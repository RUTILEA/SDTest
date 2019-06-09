from PyQt5.QtWidgets import QDialog, QGraphicsScene, QGraphicsItem, QGraphicsPixmapItem, QGraphicsRectItem, qApp
from PyQt5.QtGui import QPixmap, QCursor, QPainter, QTransform
from PyQt5.QtCore import QRectF, QSize, Qt, pyqtSignal
from view.ui.select_area_dialog import Ui_SelectAreaDialog
from model.dataset import Dataset
import os, cv2
from pathlib import Path

class SelectAreaDialog(QDialog):

    finish_selecting_area = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.ui = Ui_SelectAreaDialog()
        self.ui.setupUi(self)

        self.width = 200
        self.height = 200
        self.h, self.w = None, None
        self.select_area = None
        self.original_image_scene = None
        self.size_flag = True

        self.get_ng_sample_image_path()

        if self.h <= self.height and self.w <= self.width:
            self.size_flag = False

        if self.size_flag:
            self.show_select_area_at_default_position()
        else:
            self.ui.notation_label.setText('この画像サイズは十分小さいため, 画像全体でトレーニングを行います.'
                                           '\nこのまま完了ボタンを押してください.')
            # self.ui.notation_label.setMaximumsize()
            pass


        self.ui.ok_button.clicked.connect(self.on_clicked_ok_button)
        self.ui.cancel_button.clicked.connect(self.on_clicked_cancel_button)

        # self.original_image_scene.on_mouse_released.connect(self.test)
        # print(self.original_image_shape)
        # print(self.original_image_scene.sceneRect())
        # print(self.size())
        # print(self.ui.original_image_view.maximumSize())
        # print(self.ui.original_image_view.baseSize())

    def get_ng_sample_image_path(self):
        test_ng_path = str(Dataset.images_path(Dataset.Category.TEST_NG))
        test_ng_images = os.listdir(test_ng_path)
        test_ng_images = [img for img in test_ng_images if Path(img).suffix in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']]
        if not test_ng_images:
            return
        original_image_path = os.path.join(test_ng_path, test_ng_images[0])
        original_image = cv2.imread(original_image_path)
        # print(original_image.shape)
        h, w, c = original_image.shape
        self.h, self.w = h, w
        original_image_shape = QSize(w+10, h+11)
        # original_image_rect = QRectF(0, 0, w, h)
        original_image_item = QGraphicsPixmapItem(QPixmap(original_image_path))
        original_image_item.setZValue(0)
        self.original_image_scene = OriginalImageScene(self)
        self.original_image_scene.addItem(original_image_item)
        self.ui.original_image_view.setScene(self.original_image_scene)
        self.ui.original_image_view.setBaseSize(original_image_shape)
        self.ui.original_image_view.setMaximumSize(original_image_shape)
        # self.ui.original_image_view.fitInView(original_image_rect, Qt.KeepAspectRatioByExpanding)
        self.resize(self.w+32, self.h+72)

    def show_select_area_at_default_position(self):
        self.select_area = QGraphicsRectItem(QRectF((self.w-self.width)//2, (self.h-self.height)//2, self.width, self.height))
        self.select_area.setZValue(1)
        self.select_area.setPen(Qt.red)
        self.select_area.setFlag(QGraphicsItem.ItemIsMovable, True)
        print(self.select_area.pos())
        self.original_image_scene.addItem(self.select_area)

    # def test(self, position):   # for debug
    #     print('released')
    #     print(self.select_area.pos())

    def on_clicked_ok_button(self):
        print('zahyo and size')
        if not self.size_flag:
            position = (0, 0)
        else:
            rel_position = self.select_area.pos()
            position = (self.w//2-100+rel_position.x(), self.h//2-100+rel_position.y())
        print(position)
        if position[0] < 0 or position[0] > self.w - 201 or position[1] < 0 or position[1] > self.h - 201:
            print('Error: Please set area contained in the image.')
        else:
            self.finish_selecting_area.emit((position, (self.width, self.height)))
            print('emitted!')

    def on_clicked_cancel_button(self):
        self.close()

    def closeEvent(self, QCloseEvent):
        self.close()


class OriginalImageScene(QGraphicsScene):

    # on_mouse_released = pyqtSignal(tuple)

    def __init__(self, *argv, **keywords):
        super(OriginalImageScene, self).__init__(*argv, **keywords)
        self.parent_view = self.parent()

    # def mouseReleaseEvent(self, event):
    #     cursor = QCursor.pos()
    #     dialog_geometry = self.parent_view.geometry()
    #     view_geometry = self.parent_view.ui.original_image_view.geometry()
    #     # print("pressed here: " + str(cursor.x()) + ", " + str(cursor.y()))
    #     # print("dialog geo: " + str(dialog_geometry.x()) + ", " + str(dialog_geometry.y()))
    #     # print("view geo: " + str(view_geometry.x()) + ", " + str(view_geometry.y()))
    #
    #     position = (cursor.x() - view_geometry.x() - dialog_geometry.x()-1,
    #                 cursor.y() - view_geometry.y() - dialog_geometry.y()-1)
    #     print(position)
    #
    #     self.on_mouse_released.emit(position)

