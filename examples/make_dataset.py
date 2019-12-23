import cv2
import numpy as np
from datetime import datetime
import os
from pathlib import Path
import math


def adjust(img, alpha=1.0, beta=0.0):
    # 積和演算を行う。
    dst = alpha * img + beta
    # [0, 255] でクリップし、uint8 型にする。
    return np.clip(dst, 0, 255).astype(np.uint8)


def capture_camera(mirror=True, size=(960, 720)):
    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0)
    # 0はカメラのデバイス番号


    timestamp = str(datetime.now().isoformat()).replace(':', '-')[0:-7]
    basedir = 'testimages'
    datasetname = 'dice'
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

    gcd = math.gcd(size[0], size[1])
    aspect = size[0]/gcd, size[1]/gcd
    if aspect == (16, 9):
        print('16:9')
    elif aspect == (4, 3):
        print('4:3')
    else:
        print('cannot use guide line')

    while True:
        # retは画像を取得成功フラグ
        _, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:, ::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        # カメラガイド

        guide = cv2.imread('view_finder_960_720_full.png', -1)
        width, height = guide.shape[0:2]
        mask = guide[:, :, 3]  # アルファチャンネルだけ抜き出す。
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # 3色分に増やす。
        mask = mask / 255.0  # 0-255だと使い勝手が悪いので、0.0-1.0に変更。
        guide = guide[:, :, :3]  # アルファチャンネルは取り出しちゃったのでもういらない。

        finder = (frame[:width:, :height, :] * (1.0 - mask)).astype(np.uint8)  # 透過率に応じて元の画像を暗くする。
        finder = (finder[:width:, :height, :] + (guide * mask)).astype(np.uint8)   # 貼り付ける方の画像に透過率をかけて加算。

        # フレームを表示する
        cv2.imshow('camera capture', finder)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
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
        else:
            continue


    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()


capture_camera()
