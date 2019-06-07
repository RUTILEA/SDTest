from PyQt5.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap
from view.ui.select_area_dialog import Ui_SelectAreaDialog
from view.camera_list import CameraList
from model.camera_model import CameraModel
from PyQt5.QtMultimedia import QCamera
from typing import Dict
from model.dataset import Dataset
import os
from pathlib import Path


class SelectAreaDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SelectAreaDialog()
        self.ui.setupUi(self)

        self.ui.ok_button.clicked.connect(self.on_clicked_ok_button)

        self.ui.cancel_button.clicked.connect(self.on_clicked_cancel_button)

        self.camera_model = CameraModel.default()
        self.camera_model.cams: Dict[str, QCamera]
        self.select_camera_widget = CameraList()
        self.select_camera_widget.clicked.connect(self.on_clicked_camera_list)
        self.select_camera_widget.closed.connect(self.on_closed_camera_list)
        self.ui.select_camera_button.clicked.connect(self.on_clicked_select_camera_button)

        test_ng_path = str(Dataset.images_path(Dataset.Category.TEST_NG))
        test_ng_images = os.listdir(test_ng_path)
        test_ng_images = [img for img in test_ng_images if Path(img).suffix in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']]
        # print(test_ng_images)
        original_image_path = os.path.join(test_ng_path,test_ng_images[0])
        # self.ui.original_image_view.setFile(original_image_path)
        # self.ui.original_image_view.setImg(os.path.join(test_ng_path,test_ng_images[0]))

        self.original_image_scene = QGraphicsScene()
        self.original_image_scene.addItem(QGraphicsPixmapItem(QPixmap(original_image_path)))
        self.ui.original_image_view.setScene(self.original_image_scene)


    def on_clicked_ok_button(self):
        print('zahyo and size')

    def on_clicked_cancel_button(self):
        print('no zahyo niether size')

    def closeEvent(self, QCloseEvent):
        pass
        # self.camera_model.stop()

    def on_clicked_select_camera_button(self):
        print('TODO: on clicked camera button')
        # if self.select_camera_widget.isHidden():
        #     self.select_camera_widget = CameraList()
        #     self.select_camera_widget.clicked.connect(self.on_clicked_camera_list)
        #     self.select_camera_widget.closed.connect(self.on_closed_camera_list)
        #     self.select_camera_widget.show()
        # else:
        #     self.select_camera_widget.activateWindow()
        #     self.select_camera_widget.raise_()

    def on_clicked_camera_list(self, camera_name):
        print('TODO: on clicked camera list')
        # self.camera_model.selected_cam_names = [camera_name]
        # self.camera_model.set_selected_camera_to_view_finder(self.view_finder)

    def on_closed_camera_list(self):
        print('TODO: on cloased camera list')
        # self.camera_model.set_selected_camera_to_view_finder(self.view_finder)

