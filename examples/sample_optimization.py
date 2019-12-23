import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
from sklearn.decomposition import PCA

sys.path.append(os.path.join(os.path.dirname(__file__), '../src/main/python/module'))
from module.novelty_detector import NoveltyDetector
from module.trimming_data import TrimmingData
from scipy.stats import median_absolute_deviation as mad, median_test, mannwhitneyu as U_test
from statistics import median, stdev, mean
from math import sqrt
import csv
from pathlib import Path
from datetime import datetime
from shutil import move, copy2
import imageio


def execute_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        default='testimages/kakipi',
                        help='''path to image directory like examples/testimages/campbelle.
                        Expect path/train/OK, path/test/OK, and path/test/NG exist''',
                        type=str)

    parser.add_argument('-n','--nn',
                        nargs='?',
                        default='vgg',
                        help='''Select neural network model among Xception, ResNet(Default),
                        InceptionV3, InceptionResNetV2, MobileNet, MobileNetV2, DenseNet, NASNet''',
                        type=str)

    parser.add_argument('-l', '--layer',
                        nargs='?',
                        default=18,
                        help='Select which layer to use as feature. Less channels work better.',
                        type=int)
    
    parser.add_argument('-d', '--detector',
                        default='svm',
                        help='Select novelty detector among RobustCovariance, IsolationForest, LocalOutlierFactor, ABOD, kNN',
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

    parser.add_argument('-tr', '--trim',
                        action='store_true',
                        help='find directory, OKtrim, NGtrim')

    parser.add_argument('-c', '--center',
                        action='store_true',
                        help='trim at center point')

    # parser.add_argument('-tsize', '--trimming_size',
    #                     default=(224, 224),
    #                     help='trim at center point',
    #                     type=tuple)

    parser.add_argument('-ap', '--anchor_point',
                        default=(0, 0),
                        help='',
                        type=tuple)
                            
    args = parser.parse_args()

    if args.trim:
        Path(f'{args.path}/test/NGtrim').mkdir(exist_ok=True)
        Path(f'{args.path}/test/OKtrim').mkdir(exist_ok=True)
        Path(f'{args.path}/train/OKtrim').mkdir(exist_ok=True)
        trainok_preprocess = (os.path.join(args.path, 'train', 'OK'), os.path.dirname(os.path.join(args.path, 'train', 'OK')), 'OK')
        testok_preprocess = (os.path.join(args.path, 'test', 'OK'), os.path.dirname(os.path.join(args.path, 'test', 'OK')), 'OK')
        testng_preprocess = (os.path.join(args.path, 'test', 'NG'), os.path.dirname(os.path.join(args.path, 'test', 'NG')), 'NG')
        preprocess_pathlist = [trainok_preprocess, testok_preprocess, testng_preprocess]

        if args.nn == 'vgg':
            tr_width, tr_height = (200, 200)
        elif args.nn in ['MobileNet', 'MobileNetV2']:
            tr_width, tr_height = (224, 224)
        else:
            tr_width, tr_height = int(args.trimming_size[0]), int(args.trimming_size[1])

        for preprocess_path in preprocess_pathlist:
            p = Path(preprocess_path[0])
            preprocess_imgpathlist = list(p.glob("*"))
            for preprocess_imgpath_posix in preprocess_imgpathlist:
                preprocess_imgpath = str(preprocess_imgpath_posix)
                # print(preprocess_imgpath)
                _, ext = os.path.splitext(preprocess_imgpath)

                file_name = f'cropped_{os.path.basename(preprocess_imgpath)}'
                trimmed_image_path = os.path.join(preprocess_path[1], preprocess_path[2] + 'trim', file_name)
                # copy2(imgpath, copied_image_path)
                im = imageio.imread(preprocess_imgpath)
                im_width, im_height = im.shape[1], im.shape[0]
                # tr_width, tr_height = int(args.trimming_size[0]), int(args.trimming_size[1])
                trimming = not (im_width <= tr_width and im_height <= tr_height)

                if args.center:
                    trimming_data = TrimmingData((((im_width - tr_width) / 2), ((im_height - tr_height) / 2)),
                                                 (tr_width, tr_height), trimming)
                else:
                    trimming_data = TrimmingData(args.anchor_point, args.trimming_size, trimming)

                position = trimming_data.position
                size = trimming_data.size
                rect = im[int(position[1]):int(position[1]) + size[1], int(position[0]):int(position[0]) + size[0]]
                imageio.imwrite(trimmed_image_path, rect)

        trainok_path = os.path.join(preprocess_pathlist[0][1], 'OKtrim')
        testok_path = os.path.join(preprocess_pathlist[1][1], 'OKtrim')
        testng_path = os.path.join(preprocess_pathlist[2][1], 'NGtrim')

    else:
        trainok_path = os.path.join(args.path, 'train', 'OK')
        testok_path = os.path.join(args.path, 'test', 'OK')
        testng_path = os.path.join(args.path, 'test', 'NG')

    if not os.path.exists(trainok_path):
        print(trainok_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testok_path):
        print(testok_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testng_path):
        print(testng_path, 'does not exist')
        sys.exit(1)

    Path('learned_weight').mkdir(exist_ok=True)

    if args.layer != 18:
        layer = args.layer
    elif args.nn in ['vgg']:
        layer = 18
    elif args.nn in ['MobileNet', 'MobileNetV2']:
        layer = 95
    else:
        layer = args.layer

    model_temp = NoveltyDetector(nth_layer=layer, nn_name=args.nn, detector_name=args.detector, pool=args.pool, pca_n_components=args.pca)
    model_temp.fit_in_dir(trainok_path)
    timestamp = str(datetime.now().isoformat()).replace(':', '-')[0:-7]
    datasetname = args.path.split('/')[-1]
    weight_name = f'learned_weight/{datasetname}_{timestamp}.joblib'
    model_temp.save(weight_name)
    _, trainok_dists_temp = model_temp.predict_in_dir(trainok_path)

    model = NoveltyDetector(nth_layer=layer, nn_name=args.nn, detector_name=args.detector, pool=args.pool, pca_n_components=args.pca)
    model.load(weight_name)
    trainok_paths, trainok_dists = model.predict_in_dir(trainok_path)
    assert (model_temp.clf.get_params() == model.clf.get_params())
    assert (trainok_dists_temp == trainok_dists).all()
    testok_paths, testok_dists = model.predict_in_dir(testok_path)
    testng_paths, testng_dists = model.predict_in_dir(testng_path)
    print('The number of images')
    print('TRAIN OK:', len(trainok_paths))
    print('TEST OK:', len(testok_paths))
    print('TEST NG:', len(testng_paths))
    print('Length of features:', model.extracting_model.output_shape)
    print()

    trainok_paths = model._get_paths_in_dir(trainok_path)
    train_imgs = model._read_imgs(trainok_paths)

    train_features = model.extracting_model.predict(train_imgs)
    train_dists = model.clf.decision_function(train_features)


    # Count how many normal items are classified correctly
    thr = args.threshold
    if thr is None:
        thr = testng_dists.max()

    print('Threshold was', thr)
    false_positives_idx = np.where(testok_dists <= thr)[0]
    true_negatives_idx = np.where(testok_dists > thr)[0]
    true_positives_idx = np.where(testng_dists <= thr)[0]
    false_negatives_idx = np.where(testng_dists > thr)[0]
    print(len(false_positives_idx), ' normal items were predicted as anomaly')
    print(len(true_negatives_idx), ' normal items were predicted as normal')
    print(len(true_positives_idx), ' anormaly items were predicted as anormaly')
    print(len(false_negatives_idx), ' anormaly items were predicted as normal')
    print()

    # Verbose
    if args.verbose:
        print('Signed distance of TEST OK images')
        for path, dist in sorted(zip(testok_paths, testok_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))
        print()
        print('Signed distance of TEST NG images')
        for path, dist in sorted(zip(testng_paths, testng_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))
        print()
        
        if len(false_positives_idx) > 0:
            print('Normal image but predicted as anormaly')
            for idx in false_positives_idx:
                print(testok_paths[idx])
        else:
            print('All normal images were predicted as normal')
        print()

        if len(false_negatives_idx) > 0:
            print('Anormaly image but predicted as normal')
            for idx in false_negatives_idx:
                print(testng_paths[idx])
        else:
            print('All anormaly image were predicted as anormaly')
        print()

    # t-SNE visualization
    if args.visualization:
        from sklearn.manifold import TSNE
        trainok_imgs = model._read_imgs(trainok_paths)
        testok_imgs = model._read_imgs(testok_paths)
        testng_imgs = model._read_imgs(testng_paths)
        trainok_features = model.extracting_model.predict(trainok_imgs)
        testok_features = model.extracting_model.predict(testok_imgs)
        testng_features = model.extracting_model.predict(testng_imgs)

        tsne = TSNE(n_components=2)
        concat = np.concatenate([train_ok_features, testok_features, testng_features])
        transformed = tsne.fit_transform(concat)
        train_ok2 = transformed[:len(trainok_features)]
        test_ok2 = transformed[len(trainok_features):len(testok_features)]
        test_ng2 = transformed[len(testok_features):]
        plt.figure()
        sns.scatterplot(x=train_ok2[:, 0], y=train_ok2[:, 1], label='TRAIN OK')
        sns.scatterplot(x=test_ok2[:, 0], y=test_ok2[:, 1], label='TEST OK')
        sns.scatterplot(x=test_ng2[:, 0], y=test_ng2[:, 1], label='TEST NG')
        plt.title('Features reduced by t-SNE')
        plt.show()

    plt.figure()
    sns.distplot(trainok_dists, kde=False, rug=False, label='TRAIN OK')
    sns.distplot(testok_dists, kde=False, rug=False, label='TEST OK')
    sns.distplot(testng_dists, kde=False, rug=False, label='TEST NG')
    plt.title('Novelty detection on {}th layer on {} and {}'.format(
        layer, args.nn, args.detector)
    )
    plt.xlabel('Signed distance to hyper plane')
    plt.ylabel('a.u.')
    plt.legend()
    if args.file_name:
        plt.savefig(args.file_name)
    else:
        plt.show()

'''
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
        # writer.writerow(['work', 'fitting', 'T', 'trT', 'teT', 'F', 'med_T', 'med_trT', 'med_teT', 'med_F', 'U_test_p', 'median_test_p'])
        writer.writerow([os.path.basename(os.path.dirname(args.path)), None, T, trT, teT, F, med_T, med_trT, med_teT, med_F, u_p, med_p])
    '''

if __name__ == '__main__':
    execute_cmdline()
