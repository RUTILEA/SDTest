# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/SDTest/src/main/python/view/ui/select_area_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
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
        self.original_image_view = QtWidgets.QGraphicsView(SelectAreaDialog)
        self.original_image_view.setObjectName("original_image_view")
        self.verticalLayout_2.addWidget(self.original_image_view)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_camera_button = QtWidgets.QPushButton(SelectAreaDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_camera_button.sizePolicy().hasHeightForWidth())
        self.select_camera_button.setSizePolicy(sizePolicy)
        self.select_camera_button.setStyleSheet("padding: 3px 20px;")
        self.select_camera_button.setObjectName("select_camera_button")
        self.horizontalLayout_2.addWidget(self.select_camera_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
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
        self.select_camera_button.setText(_translate("SelectAreaDialog", "カメラを変更"))
        self.cancel_button.setText(_translate("SelectAreaDialog", "キャンセル"))
        self.ok_button.setText(_translate("SelectAreaDialog", "完了"))


