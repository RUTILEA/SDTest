from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QPainter, QColor, QPen


class QCameraViewFinderWithGuide(QCameraViewfinder):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.needs_guide = True

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.needs_guide and super().mediaObject():
            painter = QPainter(self)
            LINE_LENGTH_RATE = 30/326
            line_length = LINE_LENGTH_RATE * self.width()
            pen = QPen(QColor('#ffa00e'))
            pen.setWidth(4)
            painter.setPen(pen)
            painter.drawLine(super().width()/2, super().height()/2,
                             super().width()/2 + line_length, super().height()/2)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2 - line_length, super().height() / 2)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2, super().height() / 2 + line_length)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2, super().height() / 2 - line_length)