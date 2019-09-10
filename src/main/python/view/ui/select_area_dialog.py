# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_area_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectAreaDialog(object):
    def setupUi(self, SelectAreaDialog):
        SelectAreaDialog.setObjectName("SelectAreaDialog")
        SelectAreaDialog.resize(670, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectAreaDialog.sizePolicy().hasHeightForWidth())
        SelectAreaDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        SelectAreaDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectAreaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(SelectAreaDialog)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.original_image_view = QtWidgets.QGraphicsView(SelectAreaDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_image_view.sizePolicy().hasHeightForWidth())
        self.original_image_view.setSizePolicy(sizePolicy)
        self.original_image_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.original_image_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.original_image_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.original_image_view.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.original_image_view.setObjectName("original_image_view")
        self.horizontalLayout_2.addWidget(self.original_image_view)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.notation_label = QtWidgets.QLabel(SelectAreaDialog)
        self.notation_label.setText("")
        self.notation_label.setScaledContents(False)
        self.notation_label.setObjectName("notation_label")
        self.verticalLayout_2.addWidget(self.notation_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(SelectAreaDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.ok_button = QtWidgets.QPushButton(SelectAreaDialog)
        self.ok_button.setDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(SelectAreaDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectAreaDialog)

    def retranslateUi(self, SelectAreaDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectAreaDialog.setWindowTitle(_translate("SelectAreaDialog", "領域を選択"))
        self.label.setText(_translate("SelectAreaDialog", "<html><head/><body><p><span style=\" font-family:\'.Hiragino Kaku Gothic Interface\';\">傷や汚れ等、欠陥が発生しやすい領域</span>を指定してください。<br/>検品の際、画像内の指定された領域に異常がないか検証し、良品か不良品かを判定します。</p></body></html>"))
        self.cancel_button.setText(_translate("SelectAreaDialog", "キャンセル"))
        self.ok_button.setText(_translate("SelectAreaDialog", "トレーニング開始"))

