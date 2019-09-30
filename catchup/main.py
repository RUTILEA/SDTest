from view.start import StartWidget
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtGui import QGuiApplication
import sys

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    app_engine = QQmlApplicationEngine()
    start_widget = StartWidget(app_engine)
    start_widget.show()
    sys.exit(app.exec_())
