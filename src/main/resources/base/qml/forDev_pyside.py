import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl, Qt


# PySide2.QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
# PySide2.QtCore.Qt.ApplicationAttribute.

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    engine = QQmlApplicationEngine()
    engine.load(QUrl("main_window.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
