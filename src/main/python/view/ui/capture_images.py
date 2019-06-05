# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/SDTest/src/main/python/view/ui/capture_images.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaptureImages(object):
    def setupUi(self, CaptureImages):
        CaptureImages.setObjectName("CaptureImages")
        CaptureImages.resize(670, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CaptureImages.sizePolicy().hasHeightForWidth())
        CaptureImages.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        CaptureImages.setFont(font)
        CaptureImages.setStyleSheet("QPushButton#capture_button\n"
"{\n"
"   margin: 0 10;\n"
"   padding: 0 0;\n"
"   background-color: #3e3e3e;\n"
"   border: 1px solid #3e3e3e;\n"
"   border-radius: 25px;\n"
"   color: #f5f5f5;\n"
"   height:40px;\n"
"}\n"
"\n"
"QPushButton:pressed#capture_button\n"
"{\n"
"   background-color: #4298F9;\n"
"   border: 1px solid #4298F9;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(CaptureImages)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grid = QtWidgets.QGridLayout()
        self.grid.setObjectName("grid")
        self.verticalLayout_2.addLayout(self.grid)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_camera_button = QtWidgets.QPushButton(CaptureImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_camera_button.sizePolicy().hasHeightForWidth())
        self.select_camera_button.setSizePolicy(sizePolicy)
        self.select_camera_button.setStyleSheet("padding: 3px 20px;")
        self.select_camera_button.setAutoDefault(False)
        self.select_camera_button.setObjectName("select_camera_button")
        self.horizontalLayout_2.addWidget(self.select_camera_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.capture_button = QtWidgets.QPushButton(CaptureImages)
        self.capture_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capture_button.sizePolicy().hasHeightForWidth())
        self.capture_button.setSizePolicy(sizePolicy)
        self.capture_button.setMinimumSize(QtCore.QSize(114, 50))
        self.capture_button.setMaximumSize(QtCore.QSize(114, 50))
        self.capture_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_camera_32_4_f5f5f5_none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.capture_button.setIcon(icon)
        self.capture_button.setIconSize(QtCore.QSize(24, 24))
        self.capture_button.setAutoDefault(False)
        self.capture_button.setObjectName("capture_button")
        self.horizontalLayout.addWidget(self.capture_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(CaptureImages)
        QtCore.QMetaObject.connectSlotsByName(CaptureImages)

    def retranslateUi(self, CaptureImages):
        _translate = QtCore.QCoreApplication.translate
        CaptureImages.setWindowTitle(_translate("CaptureImages", "カメラで撮影"))
        self.select_camera_button.setText(_translate("CaptureImages", "カメラを変更"))


from qrc import icon_rc
