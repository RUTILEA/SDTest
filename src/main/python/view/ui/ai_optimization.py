# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/SDTest/src/main/python/view/ui/ai_optimization.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AIOptimization(object):
    def setupUi(self, AIOptimization):
        AIOptimization.setObjectName("AIOptimization")
        AIOptimization.resize(842, 532)
        AIOptimization.setMinimumSize(QtCore.QSize(842, 532))
        font = QtGui.QFont()
        font.setPointSize(9)
        AIOptimization.setFont(font)
        AIOptimization.setStyleSheet("")
        self.main_area = QtWidgets.QVBoxLayout(AIOptimization)
        self.main_area.setObjectName("main_area")
        self.tab_widget = QtWidgets.QTabWidget(AIOptimization)
        self.tab_widget.setStyleSheet("")
        self.tab_widget.setObjectName("tab_widget")
        self.dataset_tab = DatasetWidget()
        self.dataset_tab.setStyleSheet("")
        self.dataset_tab.setObjectName("dataset_tab")
        self.tab_widget.addTab(self.dataset_tab, "")
        self.test_tab = TestWidget()
        self.test_tab.setStyleSheet("")
        self.test_tab.setObjectName("test_tab")
        self.tab_widget.addTab(self.test_tab, "")
        self.main_area.addWidget(self.tab_widget)

        self.retranslateUi(AIOptimization)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AIOptimization)

    def retranslateUi(self, AIOptimization):
        _translate = QtCore.QCoreApplication.translate
        AIOptimization.setWindowTitle(_translate("AIOptimization", "学習"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.dataset_tab), _translate("AIOptimization", "データセットの管理とトレーニング"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.test_tab), _translate("AIOptimization", "性能評価"))


from src.view.dataset import DatasetWidget
from src.view.test import TestWidget
