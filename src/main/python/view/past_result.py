from view.ui.past_result import Ui_past_result
from model.project import Project
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem
import webbrowser, os, datetime
from pathlib import Path

class PastResultWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_past_result()
        self.ui.setupUi(self)
        self.tree=self.ui.past_result_tree_widget
        # for item in DUMMY_DATA:
        #     QTreeWidget.addTopLevelItem(self.tree,QTreeWidgetItem(item))
        self.tree.itemDoubleClicked.connect(self.on_item_clicked)
        self.inspection_results_path = os.path.join(Project.project_path(), 'inspection_results')
        self._reload_reports(self.inspection_results_path)

    def _reload_reports(self, reports_directory: Path):
        for item in os.listdir(reports_directory):
            if os.path.splitext(item)[-1] in ['.html','.htm']:
                date = str(datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(reports_directory,item)))).split(' ')[0]
                QTreeWidget.addTopLevelItem(self.tree,QTreeWidgetItem([item, date]))
        self.tree.itemDoubleClicked.connect(self.on_item_clicked)

    def on_item_clicked(self,it,col):
        report_name = it.text(0)
        webbrowser.open('file:'+os.path.join("file:",self.inspection_results_path,report_name))
