# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_list.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CameraList(object):
    def setupUi(self, CameraList):
        CameraList.setObjectName("CameraList")
        CameraList.resize(329, 206)
        font = QtGui.QFont()
        font.setPointSize(9)
        CameraList.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(CameraList)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid = QtWidgets.QGridLayout()
        self.grid.setObjectName("grid")
        self.verticalLayout.addLayout(self.grid)

        self.retranslateUi(CameraList)
        QtCore.QMetaObject.connectSlotsByName(CameraList)

    def retranslateUi(self, CameraList):
        _translate = QtCore.QCoreApplication.translate
        CameraList.setWindowTitle(_translate("CameraList", "カメラの選択"))

