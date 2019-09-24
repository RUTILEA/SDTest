import sys, os, webbrowser
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow, QWidget, QLayout, QLabel, QFileDialog, QMessageBox
from PySide2.QtCore import Qt, QSize, QObject, Signal
from view.inspection import InspectionWidget
# from view.ai_optimization import AIOptimizationWidget
# from view.past_result import PastResultWidget
from model.project import Project
from model.learning_model import LearningModel
from model.fbs import AppInfo
from pathlib import Path
from PySide2.QtGui import QMovie

class MainWindowSignal(QObject):

    # Signal
    back_to_startup = Signal()
    back_to_new_project = Signal()

class MainWindow(QMainWindow):

    def __init__(self, app_engine, appctxt):
        super().__init__()

        self.appctxt = appctxt
        self.engine = app_engine
        self.engine.load(self.appctxt.get_resource('qml/main_window.qml'))
        self.rootObject = self.engine.rootObjects()[-1]
        print(self.engine.rootObjects())
        project_name = os.path.basename(os.path.splitext(Project().project_path())[0])
        window_title = project_name + ' - ' + AppInfo().app_name() + ' Version ' + AppInfo().version()
        self.rootObject.setProperty('title', window_title)

        # Disable maximizing window
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint)

        self.msgBox = None
        self.signal = MainWindowSignal()

        self.setup_tool_bar()
        self.setup_menu_bar()

        # 一旦レポート機能なし
        self.past_result_action.setProperty('enabled', False)
        self.past_result_action.setProperty('visible', False)

        LearningModel.default().predicting_start.connect(self.on_start_predicting)
        LearningModel.default().predicting_finished.connect(self.on_finished_predicting)
        LearningModel.default().training_start.connect(self.on_start_training)
        LearningModel.default().training_finished.connect(self.on_finished_training)

    def setup_menu_bar(self):
        self.action_new_project = self.rootObject.findChild(QObject, "newprojectaction")
        self.action_open = self.rootObject.findChild(QObject, "openaction")
        self.action_close = self.rootObject.findChild(QObject, "closeaction")
        self.action_website = self.rootObject.findChild(QObject, "websiteaction")
        self.action_version = self.rootObject.findChild(QObject, "versionaction")
        self.action_new_project.triggered.connect(self.on_triggered_action_new_project)
        self.action_open.triggered.connect(self.on_triggered_action_open)
        self.action_close.triggered.connect(self.on_triggered_action_close)
        self.action_website.triggered.connect(self.on_triggered_action_website)
        self.action_version.triggered.connect(self.on_triggered_action_version)

    def setup_tool_bar(self):
        self.topbar = self.rootObject.findChild(QObject, "topbar")
        self.inspection_action = self.rootObject.findChild(QObject, "inspectionbutton")
        self.optimization_action = self.rootObject.findChild(QObject, "optimizationbutton")
        self.past_result_action = self.rootObject.findChild(QObject, "pastresultbutton")
        self.inspection_action.clicked.connect(lambda: self.on_clicked_inspection_button())
        # self.optimization_action.clicked.connect(lambda: self.on_clicked_optimization_button())
        # self.past_result_action.clicked.connect(lambda: self.on_clicked_past_result_button())
        self.inspection_view = self.rootObject.findChild(QObject, "inspectionview")

        print(self.inspection_view)
        inspection_widget = InspectionWidget(self.engine, self.appctxt, self.inspection_view)

        try:
            self.on_clicked_inspection_button()
            self.topbar.setProperty('currentTab', 0)
            LearningModel.default().load_weights()
        except FileNotFoundError:
            self.topbar.setProperty('currentTab', 1)

        loader_gif_path = self.appctxt.get_resource('images/loader.gif')
        self.loader = QMovie(loader_gif_path)
        self.loader.start()
        self.loader_label = QLabel()
        self.loader_label.setMovie(self.loader)
        self.loader_label.hide()
        self.training_message = QLabel()

        spacer = QWidget()
        spacer.setFixedWidth(2)

        self.statusBar().addPermanentWidget(self.training_message)
        self.statusBar().addPermanentWidget(self.loader_label)
        self.statusBar().addPermanentWidget(spacer)

        self.statusBar().setSizeGripEnabled(False)

    def on_clicked_inspection_button(self):
        pass
        # self.main_stacked_widget.widget(self.inspection_widget_id).set_camera_to_camera_preview()

    # def on_clicked_optimization_button(self):
    #     pass
    #
    # def on_clicked_past_result_button(self):
    #     pass

    def on_triggered_action_open(self):
        save_location_path = QFileDialog.getOpenFileName(self, 'プロジェクトを開く', os.path.expanduser('~'),
                                                         AppInfo().app_name() + ' プロジェクト(*.sdt);;すべて(*.*)')[0]
        if not save_location_path:
            return
        Project.load_settings_file(save_location_path)
        MainWindow(self.engine, self.appctxt)
        self.rootObject.close()

    def on_triggered_action_new_project(self):
        self.signal.back_to_new_project.emit()
        # self.rootObject.close()

    def on_triggered_action_close(self):
        self.signal.back_to_startup.emit()
        self.rootObject.close()

    def on_triggered_action_website(self):
        webbrowser.open('https://www.rutilea.com/')

    def on_triggered_action_version(self):
        self.msgBox = QMessageBox()
        self.msgBox.setText(AppInfo().app_name() + '\nVersion ' + AppInfo().version() + '\n(c) ' + AppInfo().author())
        self.msgBox.setWindowTitle(AppInfo().app_name() + ' Version ' + AppInfo().version())
        self.msgBox.exec()

    def closeEvent(self, QCloseEvent):
        sys.exit()

    def on_start_predicting(self):
        self.optimization_action.setDisabled(True)

    def on_finished_predicting(self):
        self.optimization_action.setDisabled(False)

    def on_start_training(self):
        self.training_message.setText('トレーニング中')
        self.loader_label.show()
        self.inspection_action.setProperty('enabled', False)

    def on_finished_training(self):
        self.training_message.setText('')
        self.loader_label.hide()
        self.inspection_action.setProperty('enabled', True)
