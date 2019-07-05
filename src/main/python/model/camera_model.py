from module.pyuvc import uvc
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QImageEncoderSettings, QCameraInfo
from datetime import datetime
import threading
from PyQt5.QtCore import pyqtSignal, QObject, QTimer, QSize
from PyQt5.QtGui import QImage
import queue
import cv2
from matplotlib import pyplot as plt

class CameraModel(QObject):
    __default_instance = None
    """This class provides QCamObjects"""
    image_saved = pyqtSignal(str)
    get_video_image_by_timer = pyqtSignal(QImage)

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = CameraModel()
        return cls.__default_instance

    @classmethod
    def get_available_camera_names(cls) -> list:
        # print(uvc.device_list())
        # uvc.Capture(uvc.device_list()[0]["uid"])
        return [device_info['name'] for device_info in uvc.device_list()]
        # return [QCamera.deviceDescription(device_obj) for device_obj in QCamera.availableDevices()]

    def __init__(self):
        super().__init__()
        self.cams = {}
        # self.__cam_image_captures: Dict[str, QCameraImageCapture] = {}
        self.__queues = {}
        self.__old_device_list = []
        self.__fetch_cam()
        self.selected_cam_names = [self.get_available_camera_names()[0]]
        self.images = {}
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_playing_qimage)
        self.timer.start(1)
        # cv2.ocl.setUseOpenCL(False)
        try:
            default_camera_name = self.get_available_camera_names()[0]
            if default_camera_name is not '':
                self.selected_cam_names.append(default_camera_name)
        # TODO: Find correct error by using the computer which has no default camera
        except Exception:
            print('No default camera')

    def __fetch_cam(self):
        for i, device in enumerate(uvc.device_list()):
            if device['name'] not in self.__old_device_list:
                self.__queues[device['name']] = queue.Queue()
                cam = uvc.Capture(device["uid"])
                self.cams[device['name']] = cam
                print(cam.avaible_modes)
                controller_dict = dict([(c.display_name, c) for c in cam.controls])
                print(controller_dict.keys())
                if 'Auto Focus' in controller_dict:
                    controller_dict['Auto Focus'].value = 0
                print(device['name'])
                uvc_thread = threading.Thread(target=self.grab_uvc, args=(device['name'], cam))
                uvc_thread.start()
                cv2.ocl.setUseOpenCL(False)
                self.__old_device_list.append(device['name'])

    def grab_uvc(self, device_name, uvc_capture):
        width, height, fps = uvc_capture.avaible_modes[2]
        print((width, height, fps))
        uvc_capture.frame_mode = (width, height, fps)
        while True:
            frame = uvc_capture.get_frame_robust()
            self.images[device_name] = frame.img

    # def img_converter(self, image):
    #     # scale_w = float(img_width) / float(img_width)
    #     # scale_h = float(img_height) / float(img_height)
    #     # scale = min([scale_w, scale_h])
    #     #
    #     #
    #     # image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    #     image =
    #     return image

    def get_playing_qimage(self):
        if self.selected_cam_names[0] not in self.images:
            print('a')
            return
        else:
            # print(self.selected_cam_names[0])
            image = self.images[str(self.selected_cam_names[0])]
            # self.get_video_image_by_timer.emit(image)
            cv2.imshow("img", image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # print(type(image))
            # print(image.shape)
            # plt.imshow(image)
            # plt.show()
            import time
            height, width, bpc = image.shape
            bpl = bpc * width
            q_image = QImage(image.data, width, height, bpl, QImage.Format_RGB888)
            self.get_video_image_by_timer.emit(q_image)

    def capture(self, directory: str):
        # TODO: manage image name format (e.x. use Dataset.generate_image_path())
        timestamp = str(datetime.now().isoformat()).replace(':', '-')
        file_name = f'camera_{0}_{timestamp}.jpg'
        image_path = directory + '/' + file_name
        if self.images[self.selected_cam_names[0]] is not None:
            cv2.imwrite(image_path, self.images[self.selected_cam_names[0]])
            self.on_image_saved(image_path)

    def on_image_saved(self, image_path):
        RESIZED_WIDTH = 640
        img = cv2.imread(image_path)
        img_height, img_width, _ = img.shape
        RESIZED_HEIGHT = int(RESIZED_WIDTH / img_width * img_height)
        img = cv2.resize(img, (RESIZED_WIDTH, RESIZED_HEIGHT))
        cv2.imwrite(image_path, img)
        self.image_saved.emit(image_path)

    def set_selected_camera_to_view_finder(self, view_finder_obj):
        # TODO:Handle many cameras on version 2.0 or more
        if len(self.selected_cam_names) > 0:
            self.__fetch_cam()
            # cam: QCamera = self.cams[self.selected_cam_names[0]]
            # cam.setViewfinder(view_finder_obj)

    def connect_view_finders_with_all_cameras(self, selectable_camera_view_list):
        self.__fetch_cam()
        # for selectable_camera_view in selectable_camera_view_list:
        #     selectable_camera_view.set_q_cam(self.cams[selectable_camera_view.get_cam_name()])


