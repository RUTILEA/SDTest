from PyQt5.QtWidgets import QDialog, QWidget
from view.ui.camera_list import Ui_CameraList
from view.ui.selectable_camera_viewfinder import Ui_SelectableCameraView
from model.camera_model import CameraModel
from PyQt5.QtMultimedia import QCamera
from typing import Dict
from PyQt5.QtCore import pyqtSignal, QSize, QPoint
from PyQt5.QtGui import QPainter


class CameraList(QDialog):

    clicked = pyqtSignal(str)
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_CameraList()
        self.ui.setupUi(self)
        self.camera_model = CameraModel.default()
        self.camera_model.cams: Dict[str, QCamera]
        self.__camera_views = []

    def set_cams(self):
        for i, (cam_device_name) in enumerate(self.camera_model.get_available_camera_names()):
            selectable_camera_view = SelectableCameraView(cam_device_name)
            selectable_camera_view.selected.connect(self.on_selected_camera)
            self.__camera_views.append(selectable_camera_view)
            self.ui.grid.addWidget(selectable_camera_view, 0, i)
        self.camera_model.connect_view_finders_with_all_cameras(self.__camera_views)

    def on_selected_camera(self, selected_widget):
        name = selected_widget.get_cam_name()
        self.camera_model.selected_cam_names = [name]
        self.clicked.emit(name)
        for camera_view in self.__camera_views:
            if camera_view is not selected_widget:
                camera_view.un_check()
        self.close()
        for camera_view in self.__camera_views:
            self.ui.grid.removeWidget(camera_view)

    def showEvent(self, QShowEvent):
        self.set_cams()
        for camera_view in self.__camera_views:
            if camera_view.ui.camera_device_name.text() == self.camera_model.selected_cam_names[0]:
                camera_view.check()
        self.__camera_views = []

    def closeEvent(self, QCloseEvent):
        self.closed.emit()


class SelectableCameraView(QWidget):

    selected = pyqtSignal(QWidget)
    __VIEW_FINDER_VIEW_SIZE = QSize(240, 180)
    __VIEW_FINDER_SIZE = QSize(240, 220)

    def __init__(self, cam_device_name):
        super().__init__()
        self.ui = Ui_SelectableCameraView()
        self.ui.setupUi(self)
        self.image = None
        self.ui.camera_view.setFixedSize(self.__VIEW_FINDER_SIZE)
        self.ui.camera_view.setAspectRatioMode(1)
        self.cam_device_name = cam_device_name
        self.ui.camera_device_name.setText(cam_device_name)
        self.ui.checkBox.clicked.connect(self.on_checkbox_clicked)
        CameraModel.default().get_video_image_by_timer.connect(self.set_image)

    def set_image(self, q_cams_image):
        image = q_cams_image[self.cam_device_name]
        self.setFixedSize(self.__VIEW_FINDER_SIZE)
        self.image = image.scaled(self.__VIEW_FINDER_VIEW_SIZE)
        self.update()

    def on_checkbox_clicked(self):
        if self.ui.checkBox.isChecked():
            self.selected.emit(self)

    def un_check(self):
        self.ui.checkBox.setChecked(False)

    def check(self):
        self.ui.checkBox.setChecked(True)

    def get_cam_name(self):
        return self.ui.camera_device_name.text()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QPoint(0, 0), self.image)
        qp.end()


