import sys, os, webbrowser
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QActionGroup, QLabel, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from view.ui.main_window import Ui_MainWindow
from view.inspection import InspectionWidget
from view.ai_optimization import AIOptimizationWidget
from view.past_result import PastResultWidget
from model.project import Project
from model.learning_model import LearningModel
from model.fbs import AppInfo
from pathlib import Path
from PyQt5.QtGui import QMovie


class MainWindow(QMainWindow):

    # Signal
    back_to_startup = pyqtSignal()
    back_to_new_project = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Disable maximizing window
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inspection_widget_id = None
        self.ai_optimization_widget_id = None
        self.past_result_widget_id = None

        self.msgBox = None

        self.inspection_mainwindow_size = QSize(780, 482)
        self.optimization_mainwindow_size = QSize(864, 632)#888
        self.past_result_mainwindow_size = QSize(780, 512)
        self.inspection_widget_size = QSize(740, 385)
        self.optimization_widget_size = QSize(840, 504)#864
        self.past_result_widget_size = QSize(740, 385)

        self.setup_tool_bar()
        self.setup_menu_bar()

        # 一旦レポート機能なし
        self.ui.past_result_action.setEnabled(False)
        self.ui.past_result_action.setVisible(False)

        LearningModel.default().predicting_start.connect(self.on_start_predicting)
        LearningModel.default().predicting_finished.connect(self.on_finished_predicting)
        LearningModel.default().training_start.connect(self.on_start_training)
        LearningModel.default().training_finished.connect(self.on_finished_training)

    def setup_menu_bar(self):
        self.ui.action_new_project.triggered.connect(self.on_triggered_action_new_project)
        self.ui.action_open.triggered.connect(self.on_triggered_action_open)
        self.ui.action_close.triggered.connect(self.on_triggered_action_close)
        self.ui.action_website.triggered.connect(self.on_triggered_action_website)
        self.ui.action_version.triggered.connect(self.on_triggered_action_version)

    def setup_tool_bar(self):
        self.inspection_widget_id = self.ui.main_stacked_widget.addWidget(InspectionWidget())
        self.ai_optimization_widget_id = self.ui.main_stacked_widget.addWidget(AIOptimizationWidget())
        self.past_result_widget_id = self.ui.main_stacked_widget.addWidget(PastResultWidget())
        self.ui.optimization_action.triggered.connect(self.on_clicked_optimization_button)
        self.ui.inspection_action.triggered.connect(self.on_clicked_inspection_button)
        self.ui.past_result_action.triggered.connect(self.on_clicked_past_result_button)
        self.ui.action_group = QActionGroup(self)
        self.ui.action_group.addAction(self.ui.optimization_action)
        self.ui.action_group.addAction(self.ui.inspection_action)
        self.ui.action_group.addAction(self.ui.past_result_action)
        self.ui.inspection_action.setChecked(True)
        self.ui.action_group.setExclusive(True)

        try:
            self.on_clicked_inspection_button()
            self.ui.inspection_action.setChecked(True)
            LearningModel.default().load_weights()
        except FileNotFoundError:
            self.on_clicked_optimization_button()
            self.ui.optimization_action.setChecked(True)

        appctxt = ApplicationContext()
        loader_gif_path = appctxt.get_resource('images/loader.gif')
        self.loader = QMovie(loader_gif_path)
        self.loader.start()
        self.loader_label = QLabel()
        self.loader_label.setMovie(self.loader)
        self.loader_label.hide()
        self.training_message = QLabel()

        self.statusBar().addWidget(self.training_message)

        self.statusBar().addPermanentWidget(self.training_message)
        self.statusBar().addPermanentWidget(self.loader_label)

    def on_clicked_inspection_button(self):
        self.ui.main_stacked_widget.widget(self.inspection_widget_id).set_camera_to_camera_preview()
        self.ui.main_stacked_widget.setCurrentIndex(self.inspection_widget_id)
        self.setFixedSize(self.inspection_mainwindow_size)
        self.ui.main_stacked_widget.setFixedSize(self.inspection_widget_size)

    def on_clicked_optimization_button(self):
        self.ui.main_stacked_widget.setCurrentIndex(self.ai_optimization_widget_id)
        self.setFixedSize(self.optimization_mainwindow_size)
        self.ui.main_stacked_widget.setFixedSize(self.optimization_widget_size)

    def on_clicked_past_result_button(self):
        self.ui.main_stacked_widget.setCurrentIndex(self.past_result_widget_id)
        self.setFixedSize(self.past_result_mainwindow_size)
        self.ui.main_stacked_widget.setFixedSize(self.past_result_widget_size)

    def on_triggered_action_open(self):
        save_location_path = QFileDialog.getOpenFileName(self, 'プロジェクトを開く', os.path.expanduser('~'),
                                                         AppInfo().app_name() + ' プロジェクト(*.sdt);;すべて(*.*)')[0]
        if not save_location_path:
            return
        Project.load_settings_file(save_location_path)
        project_name = os.path.basename(os.path.splitext(save_location_path)[0])
        window_title = project_name + ' - ' + AppInfo().app_name() + ' Version ' + AppInfo().version()
        self.setWindowTitle(window_title)
        self.show()
        self.setup_tool_bar()

    def on_triggered_action_new_project(self):
        self.back_to_new_project.emit()

    def on_triggered_action_close(self):
        self.back_to_startup.emit()

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
        self.ui.optimization_action.setDisabled(True)

    def on_finished_predicting(self):
        self.ui.optimization_action.setDisabled(False)

    def on_start_training(self):
        self.training_message.setText('トレーニング中')
        self.loader_label.show()
        self.ui.inspection_action.setDisabled(True)

    def on_finished_training(self):
        self.training_message.setText('')
        self.loader_label.hide()
        self.ui.inspection_action.setDisabled(False)
