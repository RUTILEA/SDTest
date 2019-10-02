from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QImageEncoderSettings, QCameraInfo
from datetime import datetime
from typing import Dict
from PyQt5.QtCore import pyqtSignal, QObject
import cv2


class CameraModel(QObject):
    __default_instance = None
    """This class provides QCamObjects"""
    image_saved = pyqtSignal(str)

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = CameraModel()
        return cls.__default_instance

    @classmethod
    def get_available_camera_names(cls) -> list:
        return [QCamera.deviceDescription(device_obj) for device_obj in QCamera.availableDevices()]

    def __init__(self):
        super().__init__()
        self.cams: Dict[str, QCamera] = {}
        self.__cam_image_captures: Dict[str, QCameraImageCapture] = {}
        self.__fetch_cam()
        self.selected_cam_names = []
        try:
            default_camera_name = QCameraInfo.defaultCamera().description()
            if default_camera_name is not '':
                self.selected_cam_names.append(default_camera_name)
        # TODO: Find correct error by using the computer which has no default camera
        except Exception:
            print('No default camera')

    def __fetch_cam(self):
        for device_obj in QCamera.availableDevices():
            cam_name = QCamera.deviceDescription(device_obj)

            cam = QCamera(device_obj)
            self.cams[str(cam_name)] = cam

            cam_image_capture = QCameraImageCapture(cam)
            cam_image_capture.setEncodingSettings(QImageEncoderSettings())
            cam_image_capture.captureDestination()
            cam_image_capture.imageSaved.connect(self.on_image_saved)
            self.__cam_image_captures[str(cam_name)] = cam_image_capture
            cam.statusChanged.connect(self.set_resolution)

    def capture(self, directory: str):
        for i, cam_name in enumerate(self.selected_cam_names):
            cap: QCameraImageCapture = self.__cam_image_captures[cam_name]
            cam: QCamera = self.cams[cam_name]
            # TODO: manage image name format (e.x. use Dataset.generate_image_path())
            timestamp = str(datetime.now().isoformat()).replace(':', '-')
            file_name = f'camera_{i}_{timestamp}.jpg'
            image_path = directory + '/' + file_name
            cam.searchAndLock()
            cap.capture(image_path)
            cam.unlock()

    def on_image_saved(self, id, image_path):
        RESIZED_WIDTH = 640
        img = cv2.imread(image_path)
        img_height, img_width, _ = img.shape
        RESIZED_HEIGHT = int(RESIZED_WIDTH / img_width * img_height)
        img = cv2.resize(img, (RESIZED_WIDTH, RESIZED_HEIGHT))
        cv2.imwrite(image_path, img)
        self.image_saved.emit(image_path)

    def start(self):
        for key, val in self.cams.items():
            val.start()

    def stop(self):
        for key, val in self.cams.items():
            val.stop()

    def set_resolution(self):
        for cam_name, cam in self.cams.items():
            image_settings = QImageEncoderSettings()
            for size in cam.supportedViewfinderResolutions():
                if 600 <= size.width() <= 700:
                    image_settings.setResolution(size.width(), size.height())
            self.__cam_image_captures[cam_name].setEncodingSettings(image_settings)

    def set_selected_camera_to_view_finder(self, view_finder_obj):
        # TODO:Handle many cameras on version 2.0 or more
        if len(self.selected_cam_names) > 0:
            self.__fetch_cam()
            cam: QCamera = self.cams[self.selected_cam_names[0]]
            cam.setViewfinder(view_finder_obj)
            self.start()

    def connect_view_finders_with_all_cameras(self, selectable_camera_view_list):
        self.__fetch_cam()
        for selectable_camera_view in selectable_camera_view_list:
            selectable_camera_view.set_q_cam(self.cams[selectable_camera_view.get_cam_name()])
        self.start()

