from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtGui import QPainter, QColor


class QCameraViewFinderWithGuide(QCameraViewfinder):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.needs_guide = True

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.needs_guide:
            painter = QPainter(self)
            painter.setPen(QColor('#3e3e3e'))
            line_length = 60
            painter.drawLine(super().width()/2, super().height()/2,
                             super().width()/2 + line_length, super().height()/2)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2 - line_length, super().height() / 2)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2, super().height() / 2 + line_length)
            painter.drawLine(super().width() / 2, super().height() / 2,
                             super().width() / 2, super().height() / 2 - line_length)