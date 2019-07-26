# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectable_camera_viewfinder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectableCameraView(object):
    def setupUi(self, SelectableCameraView):
        SelectableCameraView.setObjectName("SelectableCameraView")
        SelectableCameraView.resize(435, 283)
        font = QtGui.QFont()
        font.setPointSize(9)
        SelectableCameraView.setFont(font)
        SelectableCameraView.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectableCameraView)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_view = QCameraViewfinder(SelectableCameraView)
        self.camera_view.setStyleSheet("border: 2px solid #aaaaaa;\n"
"border-radius: 20px;\n"
"margin: 0;")
        self.camera_view.setObjectName("camera_view")
        self.verticalLayout.addWidget(self.camera_view)
        self.horizontalWidget = QtWidgets.QWidget(SelectableCameraView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.camera_device_name = QtWidgets.QLabel(self.horizontalWidget)
        self.camera_device_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.camera_device_name.setObjectName("camera_device_name")
        self.horizontalLayout_2.addWidget(self.camera_device_name)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(SelectableCameraView)
        QtCore.QMetaObject.connectSlotsByName(SelectableCameraView)

    def retranslateUi(self, SelectableCameraView):
        _translate = QtCore.QCoreApplication.translate
        SelectableCameraView.setWindowTitle(_translate("SelectableCameraView", "Form"))
        self.camera_device_name.setText(_translate("SelectableCameraView", "TextLabel"))

from PyQt5.QtMultimediaWidgets import QCameraViewfinder
