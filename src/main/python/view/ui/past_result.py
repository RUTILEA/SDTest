# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/SDTest/src/main/python/view/ui/past_result.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_past_result(object):
    def setupUi(self, past_result):
        past_result.setObjectName("past_result")
        past_result.resize(842, 588)
        past_result.setMinimumSize(QtCore.QSize(842, 588))
        past_result.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(past_result)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 781, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.past_result_tree_widget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.past_result_tree_widget.sizePolicy().hasHeightForWidth())
        self.past_result_tree_widget.setSizePolicy(sizePolicy)
        self.past_result_tree_widget.setSizeIncrement(QtCore.QSize(0, 0))
        self.past_result_tree_widget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.past_result_tree_widget.setFont(font)
        self.past_result_tree_widget.setStatusTip("")
        self.past_result_tree_widget.setWhatsThis("")
        self.past_result_tree_widget.setAutoFillBackground(False)
        self.past_result_tree_widget.setStyleSheet("color: #3e3e3e;\n"
"background-color: #f5f5f5;\n"
"alternate-background-color: #ffffff;\n"
"border: 0.5px solid #aaaaaa;\n"
"font: 14pt;\n"
"")
        self.past_result_tree_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.past_result_tree_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.past_result_tree_widget.setLineWidth(1)
        self.past_result_tree_widget.setMidLineWidth(0)
        self.past_result_tree_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.past_result_tree_widget.setAlternatingRowColors(True)
        self.past_result_tree_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.past_result_tree_widget.setIndentation(0)
        self.past_result_tree_widget.setUniformRowHeights(False)
        self.past_result_tree_widget.setAnimated(False)
        self.past_result_tree_widget.setAllColumnsShowFocus(False)
        self.past_result_tree_widget.setWordWrap(False)
        self.past_result_tree_widget.setHeaderHidden(False)
        self.past_result_tree_widget.setColumnCount(2)
        self.past_result_tree_widget.setObjectName("past_result_tree_widget")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.past_result_tree_widget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.past_result_tree_widget.headerItem().setFont(1, font)
        self.past_result_tree_widget.header().setVisible(True)
        self.past_result_tree_widget.header().setCascadingSectionResizes(True)
        self.past_result_tree_widget.header().setDefaultSectionSize(330)
        self.past_result_tree_widget.header().setHighlightSections(True)
        self.past_result_tree_widget.header().setMinimumSectionSize(18)
        self.past_result_tree_widget.header().setSortIndicatorShown(False)
        self.past_result_tree_widget.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.past_result_tree_widget)

        self.retranslateUi(past_result)
        QtCore.QMetaObject.connectSlotsByName(past_result)

    def retranslateUi(self, past_result):
        _translate = QtCore.QCoreApplication.translate
        past_result.setWindowTitle(_translate("past_result", "Form"))
        self.past_result_tree_widget.setSortingEnabled(False)
        self.past_result_tree_widget.headerItem().setText(0, _translate("past_result", "ファイル名"))
        self.past_result_tree_widget.headerItem().setText(1, _translate("past_result", "日付"))


