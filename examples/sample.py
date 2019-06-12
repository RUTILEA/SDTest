import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/main/python/module'))
from novelty_detector import NoveltyDetector


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
                        default='LocalOutlierFactor',
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

                            
    args = parser.parse_args()

    train_path = os.path.join(args.path, 'train', 'OK')
    testok_path = os.path.join(args.path, 'test', 'OK')
    testng_path = os.path.join(args.path, 'test', 'NG')

    if not os.path.exists(train_path):
        print(train_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testok_path):
        print(testok_path, 'does not exist')
        sys.exit(1)
    if not os.path.exists(testng_path):
        print(testng_path, 'does not exist')
        sys.exit(1)
    
    model = NoveltyDetector(nth_layer=args.layer, nn_name=args.nn, detector_name=args.detector)
    model.fit_in_dir(train_path)

    # If you are not interested in extracted feature vector, just use "paths, dists = model.predict_in_dir(dir_path)"
    testok_paths = model._get_paths_in_dir(testok_path)
    testng_paths = model._get_paths_in_dir(testng_path)
    testok_imgs = model._read_imgs(testok_paths)
    testng_imgs = model._read_imgs(testng_paths)
    testok_features = model.extracting_model.predict(testok_imgs)
    testng_features = model.extracting_model.predict(testng_imgs)
    testok_dists = model.clf.decision_function(testok_features)
    testng_dists = model.clf.decision_function(testng_features)

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
    sns.distplot(testok_dists, kde=True, rug=True, label='TEST OK')
    sns.distplot(testng_dists, kde=True, rug=True, label='TEST NG')
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


if __name__ == '__main__':
    execute_cmdline()
