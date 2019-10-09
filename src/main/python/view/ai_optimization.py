from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QObject
from model.learning_model import LearningModel
from view.dataset import DatasetWidget
from view.test import TestWidget


class AIOptimizationWidget(QWidget):
    def __init__(self, app_engine, appctxt, stack_view):
        super().__init__()
        self.engine = app_engine
        self.appctxt = appctxt
        self.stack_view = stack_view

        self.midbar = self.stack_view.findChild(QObject, 'midbar')
        self.dataset_view = self.stack_view.findChild(QObject, 'dataset_view')
        self.test_view = self.stack_view.findChild(QObject, 'test_view')
        dataset_widget = DatasetWidget(self.engine, self.appctxt, self.dataset_view)
        test_widget = TestWidget(self.engine, self.appctxt, self.test_view)

        # self.ui.tab_widget.currentChanged.connect(self._on_changed_current_tab)
        # LearningModel.default().training_finished.connect(self._on_finished_training)
        # LearningModel.default().test_finished.connect(self._on_finished_test)

    def _on_finished_training(self):
        self.midbar.setProperty('currentIndex', 1)

    def _on_changed_current_tab(self):
        if self.midbar.property('currentIndex') == 1:  # FIXME: refactor condition
            # self.ui.test_tab.show_loading()
            LearningModel.default().test_if_needed(predict_training=True)

    def _on_finished_test(self):
        pass
        # self.ui.test_tab.reload_test_results(show_training=True)
