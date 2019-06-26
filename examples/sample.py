import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
from sklearn.decomposition import PCA

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
                        default='knn',
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
                            
    args = parser.parse_args()

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
    
    model = NoveltyDetector(nth_layer=args.layer, nn_name=args.nn, detector_name=args.detector, pool=args.pool, pca_n_components=args.pca)
    model.fit_in_dir(trainok_path)
    trainok_paths, trainok_dists = model.predict_in_dir(trainok_path)
    testok_paths, testok_dists = model.predict_in_dir(testok_path)
    testng_paths, testng_dists = model.predict_in_dir(testng_path)
    print('The number of images')
    print('TRAIN OK:', len(trainok_paths))
    print('TEST OK:', len(testok_paths))
    print('TEST NG:', len(testng_paths))
    print('Length of features:', model.extracting_model.output_shape)

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
        trainok_imgs = model._read_imgs(trainok_paths)
        testok_imgs = model._read_imgs(testok_paths)
        testng_imgs = model._read_imgs(testng_paths)
        trainok_features = model.extracting_model.predict(trainok_imgs)
        testok_features = model.extracting_model.predict(testok_imgs)
        testng_features = model.extracting_model.predict(testng_imgs)

        tsne = TSNE(n_components=2)
        train_ok2 = tsne.fit_transform(trainok_features)
        test_ok2 = tsne.fit_transform(testok_features)
        test_ng2 = tsne.fit_transform(testng_features)
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
