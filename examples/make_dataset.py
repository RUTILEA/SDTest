import cv2
import numpy as np
from datetime import datetime
import os
from pathlib import Path
import argparse


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
                        default=(960, 720),
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

        if args.camera_guide:
            guide = cv2.imread('view_finder_960_720_full.png', -1)
            # guide_width, guide_height = guide.shape[0:2]
            # frame_width, frame_height = frame.shape[0:2]
            mask = guide[:, :, 3]
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            mask = mask / 255.0
            guide = guide[:, :, :3]
            # left_top = int(frame_width/2-guide_width/2), int(frame_height/2-guide_height/2)
            # finder = (frame[left_top[0]:left_top[0]+guide_width:,left_top[1]:left_top[1]+guide_height, :] * (1.0 - mask) + guide * mask).astype(np.uint8)
            finder = (frame * (1.0 - mask) + guide * mask).astype(np.uint8)
            cv2.imshow('camera capture', finder)
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
