from PySide2.QtWidgets import QDialog, QWidget
# from view.ui.camera_list import Ui_CameraList
# from view.ui.selectable_camera_viewfinder import Ui_SelectableCameraView
from model.camera_model import CameraModel
from PySide2.QtMultimedia import QCamera
# from PySide2.QtMultimediaWidgets import QCameraViewfinder
from typing import Dict
from PySide2.QtCore import Signal, QSize, QObject


class CameraListSignal(QObject):

    clicked = Signal(str)
    closed = Signal()


class CameraList(QDialog):

    def __init__(self, app_engine, appctxt):
        super().__init__()
        self.setModal(True)
        self.appctxt = appctxt
        self.engine = app_engine
        self.engine.load(self.appctxt.get_resource('qml/camera_list.qml'))
        self.rootObject = self.engine.rootObjects()[-1]
        self.grid = self.rootObject.findChild(QObject, 'grid')

        self.camera_model = CameraModel.default()
        self.camera_model.cams: Dict[str, QCamera]
        self.__camera_views = []

        self.show()

    def show(self):
        self.set_cams()
        for camera_view in self.__camera_views:
            if camera_view.ui.camera_device_name.text() == self.camera_model.selected_cam_names[0]:
                camera_view.check()
        self.__camera_views = []

    def set_cams(self):
        for i, (cam_device_name) in enumerate(self.camera_model.get_available_camera_names()):
            selectable_camera_view = SelectableCameraView(cam_device_name)
            selectable_camera_view.selected.connect(self.on_selected_camera)
            self.__camera_views.append(selectable_camera_view)
            selectable_camera_view.setParent(self.grid)
        self.camera_model.connect_view_finders_with_all_cameras(self.__camera_views)

    def on_selected_camera(self, selected_widget):
        cam_index = self.grid.indexOf(selected_widget)
        name = selected_widget.get_cam_name()
        self.camera_model.selected_cam_names = [name]
        self.clicked.emit(name)
        for camera_view in self.__camera_views:
            if camera_view is not selected_widget:
                camera_view.un_check()
        self.rootObject.close()
        self.grid.children = []
        # for camera_view in self.__camera_views:
        #     self.grid.removeWidget(camera_view)

    # def closeEvent(self, QCloseEvent):
    #     self.closed.emit()


class SelectableCameraView(QObject):

    selected = Signal(QWidget)
    __VIEW_FINDER_SIZE = QSize(300, 200)

    def __init__(self, cam_device_name):
        super().__init__()
        # self.ui = Ui_SelectableCameraView()
        # self.ui.setupUi(self)
        # self.ui.camera_view.setMinimumSize(self.__VIEW_FINDER_SIZE)
        # self.ui.camera_view.setAspectRatioMode(1)
        # self.ui.camera_device_name.setText(cam_device_name)
        # self.ui.checkBox.clicked.connect(self.on_checkbox_clicked)

    def set_q_cam(self, q_cam: QCamera):
        q_cam.setViewfinder(self.ui.camera_view)

    def on_checkbox_clicked(self):
        if self.ui.checkBox.isChecked():
            self.selected.emit(self)

    def un_check(self):
        pass
        # self.ui.checkBox.setChecked(False)

    def check(self):
        pass
        # self.ui.checkBox.setChecked(True)

    def get_cam_name(self):
        pass
        # return self.ui.camera_device_name.text()
