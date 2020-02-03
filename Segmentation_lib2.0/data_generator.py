import imageio
import cv2
import numpy as np
import os
from random import *

def decode_img(x):
    x *= 255
    x = x.astype(np.uint8)
    return x

def concatenate_zero(y):
    zero_channel = np.zeros((*y.shape[:-1], 1), dtype=np.uint8)
    y = np.concatenate((y, zero_channel), axis=-1)
    return y
    
def decode_prob(y):
    y = decode_img(y)
    y = concatenate_zero(y)
    y[:, :, :, 1] = 0
    return y

def random_crop(image, top, left, crop_size):
    bottom = top + crop_size[0]
    right = left + crop_size[1]
    image = image[top:bottom, left:right, :]
    return image

def get_datagen(img_path, seg_path, img_files, seg_files, img_size=(256, 256), batch_size=16, train=True):
    # img_files = os.listdir(img_path)
    # seg_files = os.listdir(seg_path)
    # img_files.sort()
    # seg_files.sort()
    for img_file, seg_file in zip(img_files, seg_files):

        img = imageio.imread(f'{img_path}/{img_file}', pilmode='RGB')
        seg = imageio.imread(f'{seg_path}/{seg_file}', pilmode='RGB')
        # print(f"\n{img_file}, {img.shape}, {seg.shape}")
        img = cv2.resize(img,(1024, 1024))
        seg = cv2.resize(seg,(1024, 1024))
        # print(f"\n{img_file}, {img.shape}, {seg.shape}")
        seg = seg[:, :, :-1]  # Drop unnecessary last channel in segmentation
        seg[:, :, 1] = 255 - seg[:, :, 0]  # Index 0: Defect, Index 1: Background
        img = img.astype(np.float)
        seg = seg.astype(np.float)
        img /= 255.
        seg /= 255.
        imgs = []
        segs = []
        t = 0
        # img_sender = []
        # seg_sender = []
        # img_sender.append(img)
        # seg_sender.append(seg)
        # temp_img = np.array(img_sender)
        # temp_seg = np.array(seg_sender)
        # yield(temp_img ,temp_seg )

        h, w, _ = img.shape
        # print(img_size)
        while True:
            # Crop
            # print(h - img_size[0])

            top = np.random.randint(0, h - img_size[0])
            left = np.random.randint(0, w - img_size[1])
            cropped_img = random_crop(img, top, left, img_size)
            cropped_seg = random_crop(seg, top, left, img_size)

            # if train:
                # Horizontal flip
                
            if random() > 0.5:
                cropped_img = cropped_img[:, ::-1, :]
                cropped_seg = cropped_seg[:, ::-1, :]
                # Vertical flip

            # if random() > 0.5:
            #     cropped_img = cropped_img[::-1, :, :]
            #     cropped_seg = cropped_seg[::-1, :, :]
                # Noise

            noise = 0.001 * np.random.randn(*cropped_img.shape)
            cropped_img += noise
            imgs.append(cropped_img)
            segs.append(cropped_seg)

            if len(imgs) == batch_size:
                imgs_temp = np.array(imgs)
                segs_temp = np.array(segs)
                # segs_temp = segs_temp*class_weight
                imgs = []
                segs = []
                yield (imgs_temp, segs_temp)
                # elif len(imgs) == batch_size*i:
                #     break

