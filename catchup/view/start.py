from view.next import NextWidget
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QObject
import sys


class StartWidget(QWidget):
    def __init__(self, app_engine):
        self.engine = app_engine
        self.rootObject = None
        self.start_button = None

    def show(self):
        self.engine.load('catchup/qml/start.qml')
        if not self.engine.rootObjects():
            sys.exit(-1)
        self.rootObject = self.engine.rootObjects()[-1]
        self.start_button = self.rootObject.findChild(QObject, "start_button")
        self.start_button.clicked.connect(lambda: self.on_clicked_start_button())

    def on_clicked_start_button(self):
        next_widget = NextWidget(self.engine)
        next_widget.show()

