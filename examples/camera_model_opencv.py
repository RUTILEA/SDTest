import cv2
import os
from datetime import datetime

timestamp = str(datetime.now().isoformat()).replace(':', '-')

def save_frame_camera_key(device_num, dir_path, basename, timestamp, ext='jpg', delay=10, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    if not cap.isOpened():
        return

    base_path = os.path.join(dir_path, basename)
    while True:
        cv2.startWindowThread()
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay)
        if key == ord('c'):
            cv2.waitKey(10)
            cv2.destroyWindow(window_name)
            cv2.imwrite('{}_{}.{}'.format(base_path, timestamp, ext), frame)
            cv2.waitKey(10)
            break


save_frame_camera_key(0, 'captured_image', 'cap', timestamp)
