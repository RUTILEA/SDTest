import os.path
from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import QObject, QUrl
from view.new_project import NewProjectWindow, NewProjectSignal
from view.main_window import MainWindow
from model.project import Project
from model.fbs import AppInfo


class StartupWindow(QWidget):
    def __init__(self, app_engine, appctxt):
        self.appctxt = appctxt
        self.engine = app_engine
        self.engine.load(self.appctxt.get_resource('qml/startup.qml'))
        self.rootObject = self.engine.rootObjects()[-1]
        self.new_project_button = self.rootObject.findChild(QObject, "newprojectbutton")
        self.new_project_button.clicked.connect(lambda: self.on_clicked_new_project_button())
        self.open_button = self.rootObject.findChild(QObject, "openbutton")
        self.open_button.clicked.connect(lambda: self.on_clicked_open_project_button())
        self.come_from_main_window_flag = False

    def on_clicked_new_project_button(self):
        new_project_window = NewProjectWindow(self.engine, self.appctxt)
        new_project_window.come_from_main_window_flag = self.come_from_main_window_flag
        new_project_window.signal.back_to_startup.connect(self.open_start_up_widget)
        new_project_window.signal.new_project_canceled.connect(self.open_start_up_widget)
        new_project_window.signal.close_old_project.connect(self.close_old_project)
        self.rootObject.close()

    def on_clicked_open_project_button(self):
        project_file_path = QFileDialog.getOpenFileName(None,
                                                        'プロジェクトを開く',
                                                        os.path.expanduser('~'),
                                                        AppInfo().app_name() + ' プロジェクト(*.sdt);;すべてのファイル(*.*)')[0]

        self.move_to_main_window(project_file_path)

    def move_to_main_window(self, project_file_path):

        if not project_file_path:
            return
        Project.load_settings_file(project_file_path)
        self.main_window = MainWindow(self.engine, self.appctxt)
        self.come_from_main_window_flag = True
        self.main_window.signal.back_to_new_project.connect(self.on_clicked_new_project_button)
        self.main_window.signal.back_to_startup.connect(self.open_start_up_widget)
        self.rootObject.close()

    def open_start_up_widget(self):
        self.__init__(self.engine, self.appctxt)

    def close_old_project(self):
        self.main_window.rootObject.close()

