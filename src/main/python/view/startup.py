# from model.project import Project
# from view.main_window import MainWindow
# from PySide2.QtWidgets import QWidget, QFileDialog
# from model.fbs import AppInfo
# import os.path
from PySide2.QtCore import QObject, QUrl
from view.new_project import NewProjectWindow
from view.main_window import MainWindow

class StartupWindow:
    def __init__(self, app_engine, appctxt):
        # self.appctxt = ApplicationContext()
        self.appctxt = appctxt
        self.engine = app_engine
        self.engine.load(self.appctxt.get_resource('qml/startup.qml'))
        self.rootObject = self.engine.rootObjects()[0]
        self.new_project_button = self.rootObject.findChild(QObject, "newprojectbutton")
        self.new_project_button.clicked.connect(lambda: self.on_clicked_new_project_button())
        self.open_button = self.rootObject.findChild(QObject, "openbutton")
        self.open_button.clicked.connect(lambda: self.on_clicked_open_project_button())
        self.new_project_window = None

        # self.ui.new_project_button.clicked.connect(self.on_clicked_new_project_button)
        # self.ui.open_project_button.clicked.connect(self.on_clicked_open_project_button)
        # self.new_project_window = NewProjectDialog()
        # self.main_window = None
        # self.new_project_window.back_to_startup.connect(self.open_start_up_widget)
        # self.new_project_window.new_project_canceled.connect(self.open_start_up_widget)
        # self.new_project_window.close_old_project.connect(self.close_old_project)

    def on_clicked_new_project_button(self):
        # self.new_project_window.setWindowTitle('新規プロジェクトを作成')
        # self.new_project_window.come_from_main_window_flag = False
        # self.new_project_window = NewProjectEngine()
        # self.engine.load(self.appctxt.get_resource('qml/new_project.qml'))
        NewProjectWindow(self.engine, self.appctxt)

    def on_clicked_open_project_button(self):
        # project_file_path = QFileDialog.getOpenFileName(self,
        #                                                 'プロジェクトを開く',
        #                                                 os.path.expanduser('~'),
        #                                                 AppInfo().app_name() + ' プロジェクト(*.sdt);;すべてのファイル(*.*)')[0]
        # if not project_file_path:
        #     return

        # self.move_to_main_window(project_file_path)
        self.move_to_main_window(None)

    def move_to_main_window(self, project_file_path):

        MainWindow(self.engine, self.appctxt)

        # Project.load_settings_file(project_file_path)
        # project_name = os.path.basename(os.path.splitext(project_file_path)[0])
        # window_title = project_name + ' - ' + AppInfo().app_name() + ' Version ' + AppInfo().version()
        #
        # self.main_window = MainWindow()
        #
        # self.main_window.setWindowTitle(window_title)
        # self.main_window.show()
        # self.close()
        # self.main_window.back_to_new_project.connect(self.new_project_window.open_new_project_widget)
        # self.main_window.back_to_startup.connect(self.open_start_up_widget)

    # def open_start_up_widget(self):
    #     self.setWindowTitle(AppInfo().app_name() + ' Version ' + AppInfo().version())
    #     if self.main_window:
    #         self.main_window = MainWindow()
    #     self.show()
    #
    # def close_old_project(self):
    #     self.main_window = self.new_project_window.main_window
