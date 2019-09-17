from model.project import Project
from view.main_window import MainWindow
from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import QRegExp, QObject, Signal
from model.fbs import AppInfo
import os.path
from PySide2.QtQml import QQmlApplicationEngine
from fbs_runtime.application_context.PySide2 import ApplicationContext


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


class NewProjectSignal(QObject):

    # Signal for cancel button
    back_to_startup = Signal()
    new_project_canceled = Signal()
    close_old_project = Signal()


class NewProjectWindow(QWidget):

    def __init__(self, app_engine, appctxt):
        self.engine = app_engine
        self.appctxt = appctxt
        self.engine.load(self.appctxt.get_resource('qml/new_project.qml'))
        self.rootObject = self.engine.rootObjects()[-1]
        # print(self.engine.rootObjects())
        # print(self.rootObject.findChild(QObject, "nextbutton"))
        self.project_name_line = self.rootObject.findChild(QObject, "projectnamefield")
        self.project_name_line.textEdited.connect(lambda: self.sync_project_name_edit(self.project_name_line.property('text')))
        self.save_location_line = self.rootObject.findChild(QObject, "pathfield")
        self.save_location_line.textEdited.connect(lambda: self.sync_save_location_edit(self.save_location_line.property('text')))
        self.reference_button = self.rootObject.findChild(QObject, "ref")
        self.reference_button.clicked.connect(lambda: self.on_clicked_reference_button())
        self.create_button = self.rootObject.findChild(QObject, "nextbutton")
        self.create_button.clicked.connect(lambda: self.on_clicked_create_button())
        self.cancel_button = self.rootObject.findChild(QObject, "cancel")
        self.cancel_button.clicked.connect(lambda: self.on_clicked_cancel_button())
        # self.save_location_line.returnPressed.connect(self.on_clicked_create_button())
        # self.project_name_line.returnPressed.connect(self.on_clicked_create_button())

        # self.set_create_button_enabled()
        self.save_location_line.setProperty('text', os.path.expanduser('~')+'/')
        # self.main_window = None
        self.come_from_main_window_flag = False

        # TODO: '/'の入力を制限(validation)
        # reg_ex = QRegExp("[^//]+")
        # validator = QRegExpValidator(reg_ex, self.project_name_line)
        # self.project_name_line.setValidator(validator)

        self.new_project_signal = NewProjectSignal()

        # self.new_project_signal.new_project_canceled.connect(self.test)


    def on_clicked_reference_button(self):
        save_location_path = QFileDialog.getExistingDirectory(None, '保存先フォルダを選択', os.path.expanduser('~'))
        if save_location_path:
            self.save_location_line.setProperty('text', save_location_path+'/')

    def on_clicked_create_button(self):
        save_location_path = self.save_location_line.property('text')
        project_name = os.path.basename(self.project_name_line.property('text'))
        dir_paths = [
            os.path.join(save_location_path, 'dataset/test/OK'),
            os.path.join(save_location_path, 'dataset/test/NG'),
            os.path.join(save_location_path, 'dataset/train/OK'),
            os.path.join(save_location_path, 'inspection_results'),
            os.path.join(save_location_path, 'inspection_results/images'),
            os.path.join(save_location_path, 'tmp'),
            os.path.join(save_location_path, 'models')
            ]
        for dir_path in dir_paths:
            os.makedirs(dir_path, exist_ok=True)

        # プロジェクトファイル作成部分
        project_path = save_location_path
        Project.generate_project_file(project_path, project_name)
        MainWindow(self.engine, self.appctxt)

        # self.new_project_signal.close_old_project.emit()
        # self.close()
        # self.main_window.back_to_new_project.connect(self.open_new_project_widget)
        # self.main_window.back_to_startup.connect(self.on_back_to_startup_signal)

    def on_clicked_cancel_button(self):
        # if self.come_from_main_window_flag:
        #     self.rootObject.close()
        #     return
        self.new_project_signal.new_project_canceled.emit()
        # print('hoge')
        self.rootObject.close()

    def sync_project_name_edit(self, text):
        project_name = text
        save_location_path = self.save_location_line.property('text')
        save_dir_path = os.path.dirname(save_location_path)
        path = os.path.join(save_dir_path, project_name)
        self.save_location_line.setProperty('text', path)
        # self.set_create_button_enabled()

    def sync_save_location_edit(self, text):
        save_location_path = text
        project_name = os.path.basename(save_location_path)
        self.project_name_line.setProperty('text', project_name)
        # self.set_create_button_enabled()

    # def set_create_button_enabled(self):
    #     if self.project_name_line.property('text'):
    #         self.create_button.setEnabled(True)
    #     elif not self.project_name_line.property('text'):
    #         self.create_button.setEnabled(False)

    def open_new_project_widget(self):
        self.come_from_main_window_flag = True
        # self.show()

    def on_back_to_startup_signal(self):
        self.new_project_signal.back_to_startup.emit()
    #     self.main_window = MainWindow()

    def test(self):
        print('huga')
