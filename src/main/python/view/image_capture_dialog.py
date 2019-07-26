from PyQt5.QtWidgets import QDialog
from view.ui.capture_images import Ui_CaptureImages
from view.camera_list import CameraList
from view.q_camera_view_finder_with_guide import QCameraViewFinderWithGuide
from model.camera_model import CameraModel
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtCore import QSize
from typing import Dict


class ImageCaptureDialog(QDialog):

    __VIEW_FINDER = QSize(320, 240)

    def __init__(self, image_save_location: str):
        super().__init__()

        self.setModal(True)
        self.ui = Ui_CaptureImages()
        self.ui.setupUi(self)
        self.camera_model = CameraModel.default()
        self.camera_model.cams: Dict[str, QCamera]
        self.image_save_location = image_save_location
        self.ui.capture_button.clicked.connect(self.on_clicked_capture_button)

        self.view_finder = QCameraViewFinderWithGuide()
        self.view_finder.setFixedSize(self.__VIEW_FINDER)
        self.ui.grid.addWidget(self.view_finder, 0, 0)
        self.camera_model.set_selected_camera_to_view_finder(self.view_finder)

        self.select_camera_widget = CameraList()
        self.select_camera_widget.clicked.connect(self.on_clicked_camera_list)
        self.select_camera_widget.closed.connect(self.on_closed_camera_list)

        self.ui.select_camera_button.clicked.connect(self.on_clicked_select_camera_button)

        # size to fit
        self.adjustSize()
        self.setFixedSize(self.size())

    def on_clicked_capture_button(self):
        self.camera_model.capture(directory=self.image_save_location)

    def closeEvent(self, QCloseEvent):
        self.camera_model.stop()

    def on_clicked_select_camera_button(self):
        if self.select_camera_widget.isHidden():
            self.select_camera_widget = CameraList()
            self.select_camera_widget.clicked.connect(self.on_clicked_camera_list)
            self.select_camera_widget.closed.connect(self.on_closed_camera_list)
            self.select_camera_widget.show()
        else:
            self.select_camera_widget.activateWindow()
            self.select_camera_widget.raise_()

    def on_clicked_camera_list(self, camera_name):
        self.camera_model.selected_cam_names = [camera_name]
        self.camera_model.set_selected_camera_to_view_finder(self.view_finder)

    def on_closed_camera_list(self):
        self.camera_model.set_selected_camera_to_view_finder(self.view_finder)
