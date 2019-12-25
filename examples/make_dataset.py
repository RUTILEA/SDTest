import cv2
import numpy as np
from datetime import datetime
import os
from pathlib import Path
import argparse
from module.CvOverlayImage import CvOverlayImage

def capture_camera():
    """Capture video from camera"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--datasetname',
                        default=None,
                        help='''name of dataset, such as dice, kakipi, gear...''',
                        type=str)

    parser.add_argument('-id', '--cameraid',
                        default=0,
                        help='''select camera. 0 is default.''',
                        type=int)

    parser.add_argument('-s', '--size',
                        default=(355, 200),
                        help=''''(width, height)''',
                        type=tuple)

    parser.add_argument('-g', '--camera_guide',
                        action='store_true',
                        help='''enable camera guide''',)

    parser.add_argument('-m', '--mirror',
                        action='store_true',
                        help='''enable mirror mode''', )

    args = parser.parse_args()

    cap = cv2.VideoCapture(args.cameraid)
    timestamp = str(datetime.now().isoformat()).replace(':', '-')[0:-7]
    basedir = 'testimages'
    if args.datasetname:
        datasetname = args.datasetname
    else:
        datasetname = input('please input a name of dataset: ')

    Path(os.path.join(basedir, datasetname)).mkdir(exist_ok=True)
    Path(os.path.join(basedir, datasetname, 'train')).mkdir(exist_ok=True)
    Path(os.path.join(basedir, datasetname, 'test')).mkdir(exist_ok=True)
    Path(os.path.join(basedir, datasetname, 'train', 'OK')).mkdir(exist_ok=True)
    Path(os.path.join(basedir, datasetname, 'test', 'OK')).mkdir(exist_ok=True)
    Path(os.path.join(basedir, datasetname, 'test', 'NG')).mkdir(exist_ok=True)

    train_OK_path = os.path.join(basedir, datasetname, 'train', 'OK')
    test_OK_path = os.path.join(basedir, datasetname, 'test', 'OK')
    test_NG_path = os.path.join(basedir, datasetname, 'test', 'NG')

    counter_train_OK, counter_test_OK, counter_test_NG = 0, 0, 0

    while True:
        _, frame = cap.read()

        if args.mirror is True:
            frame = frame[:, ::-1]

        if args.size is not None and len(args.size) == 2:
            frame = cv2.resize(frame, args.size)

        if args.camera_guide and min(args.size) >= 226:
            guide = cv2.imread("view_finder_v3.png", cv2.IMREAD_UNCHANGED)
            guide_height, guide_width = guide.shape[0:2]
            frame_height, frame_width = frame.shape[0:2]
            left_top = int(frame_width / 2 - guide_width / 2), int(frame_height / 2 - guide_height / 2)
            finder = CvOverlayImage.overlay(frame, guide, left_top)
            cv2.imshow('camera capture', finder)
        elif args.camera_guide and min(args.size) < 226:
            print('Size is too small. the size should be bigger than (226, 226)')

        else:
            cv2.imshow('camera capture', frame)

        k = cv2.waitKey(1)
        if k == 27:  # ESCで終了
            break
        elif k == 97:  # aでtrain/OKを撮影
            counter_train_OK += 1
            imagefilename = os.path.join(train_OK_path, f'img_{timestamp}_{counter_train_OK}') + '.jpg'
            cv2.imwrite(imagefilename, frame)
            continue
        elif k == 115:  # sでtest/OKを撮影
            counter_test_OK += 1
            imagefilename = os.path.join(test_OK_path, f'img_{timestamp}_{counter_test_OK}') + '.jpg'
            cv2.imwrite(imagefilename, frame)
            continue
        elif k == 100:  # dでtest/NGを撮影
            counter_test_NG += 1
            imagefilename = os.path.join(test_NG_path, f'img_{timestamp}_{counter_test_NG}') + '.jpg'
            cv2.imwrite(imagefilename, frame)
            continue

    cap.release()
    cv2.destroyAllWindows()


capture_camera()
