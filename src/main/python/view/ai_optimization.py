from PyQt5.QtWidgets import QWidget
from view.ui.ai_optimization import Ui_AIOptimization
from model.learning_model import LearningModel


class AIOptimizationWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AIOptimization()
        self.ui.setupUi(self)
        self.ui.tab_widget.currentChanged.connect(self._on_changed_current_tab)
        LearningModel.default().training_finished.connect(self._on_finished_training)
        LearningModel.default().test_finished.connect(self._on_finished_test)

    def _on_finished_training(self):
        self.ui.tab_widget.setCurrentIndex(1)

    def _on_changed_current_tab(self):
        if self.ui.tab_widget.currentIndex() == 1:  # FIXME: refactor condition
            self.ui.test_tab.show_loading()
            LearningModel.default().test_if_needed()

    def _on_finished_test(self):
        self.ui.test_tab.reload_test_results()
