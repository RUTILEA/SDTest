import os, sys
sys.path.append(os.getcwd())
from module.novelty_detector import NoveltyDetector
import argparse

def execute_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('-path',
                        default='src/module/examples/testimages/campbelle',
                        help='''path to image directory like src/module/examples/testimages/campbelle.
                        Expect path/train/OK, path/test/OK, and path/test/NG exist''',
                        type=str)
    
    parser.add_argument('-nn','--nn_name',
                        nargs='?',
                        default='ResNet',
                        help='''Select neural network model among Xception, ResNet(Default),
                        InceptionV3, InceptionResNetV2, MobileNet, MobileNetV2, DenseNet, NASNet''',
                        type=str)

    parser.add_argument('-l', '--layer',
                        required=True,
                        help='Select which layer to use as feature',
                        type=int)
    
    parser.add_argument('-detector', '--detector_name',
                        default='IsolationForest',
                        help='Select novelty detector among RobustCovariance, IsolationForest(Default), LocalOutlierFactor',
                        type=str)
    
    parser.add_argument('-img', '--image_name',
                        default=None,
                        help='Save result figure with given name if given, otherwise just show',
                        type=str)

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show signed distance of each images from hyper plane (default to False)')
                            
    args = parser.parse_args()

    train_path = os.path.join(args.path, 'train', 'OK')
    testok_path = os.path.join(args.path, 'test', 'OK')
    testng_path = os.path.join(args.path, 'test', 'NG')

    if not os.path.exists(train_path):
        print(train_path, 'does not exist')
    if not os.path.exists(testok_path):
        print(testok_path, 'does not exist')
    if not os.path.exists(testng_path):
        print(testng_path, 'does not exist')
    if not (os.path.exists(train_path) and os.path.exists(testok_path) and os.path.exists(testng_path)):
        sys.exit(1)

    
    model = NoveltyDetector(nth_layer=args.layer, nn_name=args.nn_name, detector_name=args.detector_name)
    model.fit_in_dir(train_path)
    testok_paths, testok_dists = model.predict_in_dir(testok_path)
    testng_paths, testng_dists = model.predict_in_dir(testng_path)

    if args.verbose:
        print('Signed distance of TEST OK images')
        
        for path, dist in sorted(zip(testok_paths, testok_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))
        print()
        print('Signed distance of TEST NG images')
        for path, dist in sorted(zip(testng_paths, testng_dists), key=lambda x: x[1]):
            print('{}: {:.4f}'.format(path, dist))

        
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure()
    sns.distplot(testok_dists, kde=True, rug=True, label='TEST OK')
    sns.distplot(testng_dists, kde=True, rug=True, label='TEST NG')
    plt.title('Novelty detection on {}th layer on {} and {}'.format(
        args.layer, args.nn_name, args.detector_name)
    )
    plt.xlabel('Signed distance to hyper plane')
    plt.ylabel('a.u.')
    plt.legend()
    if args.image_name:
        plt.savefig(args.image_name)
    else:
        plt.show()


if __name__ == '__main__':
    execute_cmdline()
