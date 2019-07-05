# from model.project import Project
# from view.main_window import MainWindow
# from PyQt5.QtWidgets import QWidget, QFileDialog
# from model.fbs import AppInfo
# import os.path
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QUrl
from view.new_project import NewProjectEngine
from fbs_runtime.application_context.PyQt5 import ApplicationContext


class StartupEngine(QQmlApplicationEngine):
    def __init__(self):
        QQmlApplicationEngine.__init__(self)
        appctxt = ApplicationContext()
        self.load(appctxt.get_resource('qml/startup.qml'))
        # self.load('src/main/python/view/qml/startup.qml')
        # print(self.rootObjects())
        self.rootObject = self.rootObjects()[0]
        self.new_project_button = self.rootObject.findChild(QObject, "newprojectbutton")
        self.new_project_button.clicked.connect(self.on_clicked_new_project_button)
        self.new_project_window = None

        # self.ui.new_project_button.clicked.connect(self.on_clicked_new_project_button)
        # self.ui.open_project_button.clicked.connect(self.on_clicked_open_project_button)

    def on_clicked_new_project_button(self):
        # self.new_project_window.setWindowTitle('新規プロジェクトを作成')
        # self.new_project_window.come_from_main_window_flag = False
        self.new_project_window = NewProjectEngine()
