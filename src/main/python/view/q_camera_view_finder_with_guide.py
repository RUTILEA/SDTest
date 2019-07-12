from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QPoint, QSize, QRect
from model.camera_model import CameraModel

class QCameraViewFinderWithGuide(QWidget):

    __VIEW_FINDER = QSize(320, 240)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.needs_guide = True
        self.image = None
        CameraModel.default().get_video_image_by_timer.connect(self.set_image)

    def set_image(self, q_cams_image):
        image = q_cams_image[CameraModel.default().selected_cam_names[0]]
        self.image = image.scaled(self.__VIEW_FINDER)
        self.setMinimumSize(self.__VIEW_FINDER)
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QPoint(0, 0), self.image)
        qp.end()
        # if self.needs_guide:
        #     painter = QPainter(self)
        #     LINE_LENGTH_RATE = 30/326
        #     line_length = LINE_LENGTH_RATE * self.width()
        #     pen = QPen(QColor('#ffa00e'))
        #     pen.setWidth(4)
        #     painter.setPen(pen)
        #     painter.drawLine(super().width()/2, super().height()/2,
        #                      super().width()/2 + line_length, super().height()/2)
        #     painter.drawLine(super().width() / 2, super().height() / 2,
        #                      super().width() / 2 - line_length, super().height() / 2)
        #     painter.drawLine(super().width() / 2, super().height() / 2,
        #                      super().width() / 2, super().height() / 2 + line_length)
        #     painter.drawLine(super().width() / 2, super().height() / 2,
        #                      super().width() / 2, super().height() / 2 - line_length)