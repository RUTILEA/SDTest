from PyQt5.QtCore import QObject


class TrimmingData(QObject):
    def __init__(self, position: tuple, size: tuple, needs_trimming: bool):
        super().__init__()
        self.position = position
        self.size = size
        self.needs_trimming = needs_trimming

