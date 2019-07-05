# from view.ui.new_project import Ui_NewProjectDialog
# from model.project import Project
# from view.main_window import MainWindow
# from PyQt5.QtWidgets import QWidget, QFileDialog
# from PyQt5.QtGui import QRegExpValidator
# from PyQt5.QtCore import QRegExp, pyqtSignal
# from model.fbs import AppInfo
# import os.path
from PyQt5.QtQml import QQmlApplicationEngine
from fbs_runtime.application_context.PyQt5 import ApplicationContext


'''
- プロジェクト名.sdt(プロジェクトファイル)
- dataset 
    - test 
        - OK
        - NG
    - train 
        - OK
- inspection_results
    - images 
- tmp
- models
'''


class NewProjectEngine(QQmlApplicationEngine):

    # # Signal for cancel button
    # back_to_startup = pyqtSignal()
    # new_project_canceled = pyqtSignal()
    # close_old_project = pyqtSignal()

    def __init__(self):
        QQmlApplicationEngine.__init__(self)
        appctxt = ApplicationContext()
        self.load(appctxt.get_resource('qml/new_project.qml'))
        # QWidget.__init__(self)
        # self.ui = Ui_NewProjectDialog()
        # self.ui.setupUi(self)
        # self.ui.project_name_line.textEdited.connect(self.sync_project_name_edit)
        # self.ui.save_location_line.textEdited.connect(self.sync_save_location_edit)
        # self.ui.reference_button.clicked.connect(self.on_clicked_reference_button)
        # self.ui.create_button.clicked.connect(self.on_clicked_create_button)
        # self.ui.cancel_button.clicked.connect(self.on_clicked_cancel_button)
        # self.ui.save_location_line.returnPressed.connect(self.on_clicked_create_button)
        # self.ui.project_name_line.returnPressed.connect(self.on_clicked_create_button)
        # self.set_create_button_enabled()
        # self.ui.save_location_line.setText(os.path.expanduser('~')+'/')
        # self.main_window = None
        # self.come_from_main_window_flag = False
        # # '/'の入力を制限(validation)
        # reg_ex = QRegExp("[^//]+")
        # validator = QRegExpValidator(reg_ex, self.ui.project_name_line)
        # self.ui.project_name_line.setValidator(validator)


    # def on_clicked_reference_button(self):
    #     save_location_path = QFileDialog.getExistingDirectory(self, '保存先フォルダを選択', os.path.expanduser('~'))
    #     if save_location_path:
    #         self.ui.save_location_line.setText(save_location_path+'/')
    #
    # def on_clicked_create_button(self):
    #     save_location_path = self.ui.save_location_line.text()
    #     project_name = os.path.basename(self.ui.project_name_line.text())
    #     dir_paths = [
    #         os.path.join(save_location_path, 'dataset/test/OK'),
    #         os.path.join(save_location_path, 'dataset/test/NG'),
    #         os.path.join(save_location_path, 'dataset/train/OK'),
    #         os.path.join(save_location_path, 'inspection_results'),
    #         os.path.join(save_location_path, 'inspection_results/images'),
    #         os.path.join(save_location_path, 'tmp'),
    #         os.path.join(save_location_path, 'models')
    #         ]
    #     for dir_path in dir_paths:
    #         os.makedirs(dir_path, exist_ok=True)
    #
    #     # プロジェクトファイル作成部分
    #     project_path = save_location_path
    #     Project.generate_project_file(project_path, project_name)
    #     window_title = project_name + ' - ' + AppInfo().app_name() + ' Version ' + AppInfo().version()
    #     self.main_window = MainWindow()
    #     self.main_window.setWindowTitle(window_title)
    #     self.main_window.show()
    #     self.close_old_project.emit()
    #     self.close()
    #     self.main_window.back_to_new_project.connect(self.open_new_project_widget)
    #     self.main_window.back_to_startup.connect(self.on_back_to_startup_signal)
    #
    # def on_clicked_cancel_button(self):
    #     if self.come_from_main_window_flag:
    #         self.close()
    #         return
    #     self.new_project_canceled.emit()
    #     self.close()
    #
    # def sync_project_name_edit(self, text):
    #     project_name = text
    #     save_location_path = self.ui.save_location_line.text()
    #     save_dir_path = os.path.dirname(save_location_path)
    #     path = os.path.join(save_dir_path, project_name)
    #     self.ui.save_location_line.setText(path)
    #     self.set_create_button_enabled()
    #
    # def sync_save_location_edit(self, text):
    #     save_location_path = text
    #     project_name = os.path.basename(save_location_path)
    #     self.ui.project_name_line.setText(project_name)
    #     self.set_create_button_enabled()
    #
    # def set_create_button_enabled(self):
    #     if self.ui.project_name_line.text():
    #         self.ui.create_button.setEnabled(True)
    #     elif not self.ui.project_name_line.text():
    #         self.ui.create_button.setEnabled(False)
    #
    # def open_new_project_widget(self):
    #     self.come_from_main_window_flag = True
    #     self.show()
    #
    # def on_back_to_startup_signal(self):
    #     self.back_to_startup.emit()
    #     self.main_window = MainWindow()
