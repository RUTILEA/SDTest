import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/main/python/module'))
from novelty_detector import NoveltyDetector
from scipy.stats import median_absolute_deviation as mad, median_test, mannwhitneyu as U_test
from statistics import median, stdev, mean
from math import sqrt
import csv

def execute_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        default='testimages/campbelle',
                        help='''path to image directory like examples/testimages/campbelle.
                        Expect path/train/OK, path/test/OK, and path/test/NG exist''',
                        type=str)

    parser.add_argument('-n','--nn',
                        nargs='?',
                        default='ResNet',
                        help='''Select neural network model among Xception, ResNet(Default),
                        InceptionV3, InceptionResNetV2, MobileNet, MobileNetV2, DenseNet, NASNet''',
                        type=str)

    parser.add_argument('-l', '--layer',
                        nargs='?',
                        default=24,
                        help='Select which layer to use as feature. Less channels work better.',
                        type=int)
    
    parser.add_argument('-d', '--detector',
                        default='knn',
                        help='Select novelty detector among RobustCovariance, IsolationForest, LocalOutlierFactor(Default), ABOD',
                        type=str)
    
    parser.add_argument('-f', '--file_name',
                        default=None,
                        help='Save result figure with given name if given, otherwise just show',
                        type=str)

    parser.add_argument('-vs', '--visualization',
                        action='store_true',
                        help='Show features reduced into two dimensions by t-SNE')

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show signed distance of each images from hyper plane (default to False)')

    parser.add_argument('-t', '--threshold',
                        nargs='?',
                        default=None,
                        help='Threshold to split scores of predicted items. Default to the max score of NG images',
                        type=float)

    parser.add_argument('-pl', '--pool',
                        default=None,
                        type=str)
    parser.add_argument('-pca', '--pca',
                        type=int,
                        default=None)
                            
    args = parser.parse_args()

    trainok_path = os.path.join(args.path, 'train', 'trim')
    testok_path = os.path.join(args.path, 'test', 'OKtrim')
    testng_path = os.path.join(args.path, 'test', 'NGtrim')

    if not os.path.exists(trainok_path):
        print(trainok_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testok_path):
        print(testok_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testng_path):
        print(testng_path, 'does not exist')
        sys.exit(1)
    
    model = NoveltyDetector(nth_layer=args.layer, nn_name=args.nn, detector_name=args.detector, pool=args.pool, pca=args.pca)
    model.fit_in_dir(trainok_path)

    # If you are not interested in extracted feature vector, just use "paths, dists = model.predict_in_dir(dir_path)"

    trainok_paths = model._get_paths_in_dir(trainok_path)
    testok_paths = model._get_paths_in_dir(testok_path)
    testng_paths = model._get_paths_in_dir(testng_path)
    trainok_imgs = model._read_imgs(trainok_paths)
    testok_imgs = model._read_imgs(testok_paths)
    testng_imgs = model._read_imgs(testng_paths)
    trainok_features = model.extracting_model.predict(trainok_imgs)
    testok_features = model.extracting_model.predict(testok_imgs)
    testng_features = model.extracting_model.predict(testng_imgs)
    print(testng_features.shape)

    from sklearn.decomposition import PCA
    pca = PCA(n_components=args.pca)
    if args.pca:
        trainok_features, testok_features, testng_features = map(pca.fit_transform, [trainok_features, testok_features, testng_features])
    trainok_dists = model.clf.decision_function(trainok_features)
    testok_dists = model.clf.decision_function(testok_features)
    testng_dists = model.clf.decision_function(testng_features)
    if args.detector == 'abod' or 'knn':
        trainok_dists += -1
        testok_dists *= -1
        testng_dists *= -1

    trainok_paths = model._get_paths_in_dir(trainok_path)
    train_imgs = model._read_imgs(trainok_paths)
    train_features = model.extracting_model.predict(train_imgs)
    train_dists = model.clf.decision_function(train_features)


    # Count how many normal items are classified correctly
    thr = args.threshold
    if thr is None:
        thr = testng_dists.max()

    print('Threshold was', thr)
    print(len(np.where(testok_dists < thr)[0]), ' normal items were predicted as anomaly')
    print(len(np.where(testok_dists > thr)[0]), ' normal items were predicted as normal')
    print(len(np.where(testng_dists < thr)[0]), ' anormaly items were predicted as anormaly')
    print(len(np.where(testng_dists > thr)[0]), ' anormaly items were predicted as normal')    

    # Verbose
    if args.verbose:
        print('Signed distance of TEST OK images')
        for path, dist in sorted(zip(testok_paths, testok_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))
        print()
        print('Signed distance of TEST NG images')
        for path, dist in sorted(zip(testng_paths, testng_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))

    # t-SNE visualization
    if args.visualization:
        from sklearn.manifold import TSNE
        tsne = TSNE(n_components=2)
        ok2 = tsne.fit_transform(testok_features)
        ng2 = tsne.fit_transform(testng_features)
        plt.figure()
        sns.scatterplot(x=ok2[:, 0], y=ok2[:, 1], label='TEST OK')
        sns.scatterplot(x=ng2[:, 0], y=ng2[:, 1], label='TEST NG')
        plt.title('Features reduced by t-SNE')
        plt.show()
        

    plt.figure()
    sns.distplot(trainok_dists, kde=False, rug=False, label='TRAIN OK')
    sns.distplot(testok_dists, kde=False, rug=False, label='TEST OK')
    sns.distplot(testng_dists, kde=False, rug=False, label='TEST NG')
    plt.title('Novelty detection on {}th layer on {} and {}'.format(
        args.layer, args.nn, args.detector)
    )
    plt.xlabel('Signed distance to hyper plane')
    plt.ylabel('a.u.')
    plt.legend()
    if args.file_name:
        plt.savefig(args.file_name)
    else:
        plt.show()

    # T statistics

    n = len(train_dists)
    m = len(testok_dists)

    std_train = stdev(train_dists)
    std_testok = stdev(testok_dists)
    nm = sqrt(1/n+1/m)
    s = sqrt(std_train/n+std_testok/m)
    T = abs(mean(train_dists)-mean(testok_dists))/s
    F = std_testok/std_train
    trT = abs(mean(train_dists)-mean(testok_dists))/(nm*std_train)
    teT = abs(mean(train_dists)-mean(testok_dists))/(nm*std_testok)

    print('')
    # print('mean_train:'+str(mean(train_dists)))
    print('std_train:'+str(std_train))
    # print('mean_testok:'+str(mean(testok_dists)))
    print('std_testok:'+str(std_testok))
    print('diff_mean:'+str(abs(mean(train_dists) - mean(testok_dists))))
    print('nm:'+str(nm))
    print('s:'+str(s))
    print('T:'+str(T))
    print('trT:'+str(trT))
    print('teT:'+str(teT))
    print('F:'+str(F))


    # MAD statistics

    mad_train = mad(train_dists)
    mad_testok = mad(testok_dists)
    s = sqrt(mad_train/n+mad_testok/m)
    med_T = abs(median(train_dists)-median(testok_dists))/s
    med_trT = abs(median(train_dists)-median(testok_dists))/(nm*mad_train)
    med_teT = abs(median(train_dists)-median(testok_dists))/(nm*mad_testok)
    med_F = mad_testok/mad_train

    print('')
    # print('median_train:'+str(median(train_dists)))
    print('mad_train:'+str(mad_train))
    # print('median_testok:'+str(median(testok_dists)))
    print('mad_testok:'+str(mad_testok))
    print('diff_median:'+str(abs(median(train_dists) - median(testok_dists))))
    print('nm:'+str(nm))
    print('s:'+str(s))
    print('med_T:'+str(med_T))
    print('med_trT:'+str(med_trT))
    print('med_teT:'+str(med_teT))
    print('med_F:'+str(med_F))


    # U test
    print('')
    print('U test')
    u_p = U_test(train_dists, testok_dists)[1]
    print('u_p:'+str(u_p))


    # median test
    print('')
    print('median test')
    med_p = median_test(train_dists, testok_dists)[1]
    print('med_p:'+str(med_p))

    with open('examples/hist/statistics.csv', 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(['work', 'how near dists are?', 'T', 'trT', 'teT', 'F', 'med_T', 'med_trT', 'med_teT', 'med_F', 'U_test_p', 'median_test_p'])
        writer.writerow([os.path.basename(os.path.dirname(args.path)), None, T, trT, teT, F, med_T, med_trT, med_teT, med_F, u_p, med_p])


if __name__ == '__main__':
    execute_cmdline()
