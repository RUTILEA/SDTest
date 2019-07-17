import sys
sys.path.insert(1,'/Users/r.hirokawa/PycharmProjects/SDTest_2/venv/lib/python3.6/site-packages/')
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('main_window.qml')
    sys.exit(app.exec_())
