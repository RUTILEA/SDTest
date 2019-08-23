import sys, PySide2
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QUrl, Qt
from PySide2 import QtCore

PySide2.QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'Info'
    elif mode == QtCore.QtWarningMsg:
        mode = 'Warning'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'critical'
    elif mode == QtCore.QtFatalMsg:
        mode = 'fatal'
    else:
        mode = 'Debug'
    print("%s: %s (%s:%d, %s)" % (mode, message, context.file, context.line, context.file))


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    QtCore.qInstallMessageHandler(qt_message_handler)
    engine = QQmlApplicationEngine()
    engine.load(QUrl("main_window.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
