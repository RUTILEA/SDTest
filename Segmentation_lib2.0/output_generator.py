import cv2
import imageio
import numpy as np
from PIL import Image
import os
from Unet_model import UNet

def concatenate_zero(y):
    zero_channel = np.zeros((*y.shape[:-1], 1), dtype=np.uint8)
    y = np.concatenate((y, zero_channel), axis=-1)
    return y

def run(input_path, weight_name, pre_num, result_path,pre_name):

  for num in range(pre_num[0], pre_num[1]):
    # if num == 41:
    #   continue
    img_normal_files = os.listdir(f'{input_path}')
    img_normal_files.sort()
    img = imageio.imread(f'{input_path}/{img_normal_files[num]}', pilmode ='RGB')
    # img = img[:, img.shape[1]:, :]  # image height/width should be the times of 16 because U-Net has 4 down/up-sampling.
    img = cv2.resize(img,(512,512))
    # img[0] = img[0]/10
    img = img.astype(np.float) / 255.
    print(img.shape)
    model = UNet(input_shape=img.shape, classes=2).build()
    model.load_weights(f'{weight_name}')
    img = np.array([img])  # Add BATCH_SIZE = 1 channel.
    # plt.imshow(img)
    print(num)
    # Prediction
    preds = model.predict(img)  # [1, HEIGHT, WIDTH, 2]
    pred_image = concatenate_zero(preds[0])
    pred_image[:, :, 1] = 0
    pred_image[:, :, 0] = pred_image[:, :, 0]
    # img_editor = imageio.imread(f'{input_path}/{img_normal_files[num]}', pilmode = 'RGB')
    # img_editor = cv2.resize(img_editor,(512,512))
    # img_editor = img_editor.astype(np.float) / 255.
    # pred_image = pred_image + img_editor
    # pred_image[pred_image > 1] = 1

    # fig, axes = plt.subplots(1, 3, figsize=(18, 32))

    pil_img = Image.fromarray((pred_image*255).astype(np.uint8))
    pil_img.save(f'{result_path}/{pre_name}_{num}.png')