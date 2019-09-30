from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QObject
import sys


class NextWidget(QWidget):
    def __init__(self, app_engine):
        self.engine = app_engine
        self.rootObject = None
        self.start_button = None

    def show(self):
        self.engine.load('catchup/qml/next.qml')
        if not self.engine.rootObjects():
            sys.exit(-1)
        self.rootObject = self.engine.rootObjects()[-1]
