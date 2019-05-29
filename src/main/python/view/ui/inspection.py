# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/tazama/src/view/ui/inspection.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_inspection(object):
    def setupUi(self, inspection):
        inspection.setObjectName("inspection")
        inspection.resize(842, 588)
        inspection.setMinimumSize(QtCore.QSize(842, 588))
        font = QtGui.QFont()
        font.setPointSize(9)
        inspection.setFont(font)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(inspection)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.camera_preview = QCameraViewfinder(inspection)
        self.camera_preview.setMinimumSize(QtCore.QSize(152, 102))
        self.camera_preview.setStyleSheet("background-color: #f5f5f5;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 8px;\n"
"margin: 0px;\n"
"min-width: 150px;\n"
"min-height: 100px;\n"
"")
        self.camera_preview.setObjectName("camera_preview")
        self.verticalLayout.addWidget(self.camera_preview)
        self.horizontalWidget = QtWidgets.QWidget(inspection)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.select_camera_button = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_camera_button.sizePolicy().hasHeightForWidth())
        self.select_camera_button.setSizePolicy(sizePolicy)
        self.select_camera_button.setStyleSheet("padding: auto 20px;")
        self.select_camera_button.setObjectName("select_camera_button")
        self.horizontalLayout_3.addWidget(self.select_camera_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.horizontalWidget1 = QtWidgets.QWidget(inspection)
        self.horizontalWidget1.setMinimumSize(QtCore.QSize(0, 80))
        self.horizontalWidget1.setMaximumSize(QtCore.QSize(16777215, 80))
        self.horizontalWidget1.setStyleSheet("QPushButton#inspect_button\n"
"{\n"
"   padding: 0 40px;\n"
"   border-radius: 25px;\n"
"   border: 1px solid #3e3e3e;\n"
"   color: #f5f5f5;\n"
"   height: 52px;\n"
"   background-color: #3e3e3e;\n"
"}\n"
"\n"
"QPushButton:pressed#inspect_button\n"
"{\n"
"   background-color: #4298F9;\n"
"   border: 1px solid #4298F9;\n"
"}")
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.inspect_button = QtWidgets.QPushButton(self.horizontalWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.inspect_button.setFont(font)
        self.inspect_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/ionicons_2-0-1_eye_32_4_f5f5f5_none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inspect_button.setIcon(icon)
        self.inspect_button.setIconSize(QtCore.QSize(32, 32))
        self.inspect_button.setObjectName("inspect_button")
        self.horizontalLayout_4.addWidget(self.inspect_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.horizontalWidget1)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.loader_label = QtWidgets.QLabel(inspection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loader_label.sizePolicy().hasHeightForWidth())
        self.loader_label.setSizePolicy(sizePolicy)
        self.loader_label.setMinimumSize(QtCore.QSize(30, 0))
        self.loader_label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.loader_label.setText("")
        self.loader_label.setObjectName("loader_label")
        self.horizontalLayout_7.addWidget(self.loader_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.result = QtWidgets.QStackedWidget(inspection)
        self.result.setMinimumSize(QtCore.QSize(300, 0))
        self.result.setStyleSheet("margin: 0px;")
        self.result.setObjectName("result")
        self.default_result = QtWidgets.QWidget()
        self.default_result.setAutoFillBackground(False)
        self.default_result.setStyleSheet("background-color: #f5f5f5;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 6px;\n"
"margin: 0;")
        self.default_result.setObjectName("default_result")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.default_result)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.default_label = QtWidgets.QLabel(self.default_result)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.default_label.setFont(font)
        self.default_label.setStyleSheet("color:#aaaaaa;\n"
"border:none;\n"
"")
        self.default_label.setAlignment(QtCore.Qt.AlignCenter)
        self.default_label.setObjectName("default_label")
        self.verticalLayout_3.addWidget(self.default_label)
        self.result.addWidget(self.default_result)
        self.OK = QtWidgets.QWidget()
        self.OK.setStyleSheet("background-color: #193FDA68;\n"
"border: 1px solid #3FDA68;\n"
"border-radius: 6px;\n"
"color: #3FDA68;\n"
"margin: 0;\n"
"")
        self.OK.setObjectName("OK")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.OK)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.OK_big_icon_label = QtWidgets.QLabel(self.OK)
        self.OK_big_icon_label.setStyleSheet("border: none;\n"
"background-color: #00000000;")
        self.OK_big_icon_label.setText("")
        self.OK_big_icon_label.setPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_check-circle_96_4_3fda68_none.png"))
        self.OK_big_icon_label.setScaledContents(False)
        self.OK_big_icon_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.OK_big_icon_label.setObjectName("OK_big_icon_label")
        self.verticalLayout_4.addWidget(self.OK_big_icon_label)
        self.OK_message_label = QtWidgets.QLabel(self.OK)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.OK_message_label.setFont(font)
        self.OK_message_label.setStyleSheet("color: #3FDA68;\n"
"background-color: transparent;\n"
"border: none;")
        self.OK_message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.OK_message_label.setObjectName("OK_message_label")
        self.verticalLayout_4.addWidget(self.OK_message_label)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.result.addWidget(self.OK)
        self.NG = QtWidgets.QWidget()
        self.NG.setStyleSheet("background-color: #19e66643;\n"
"border: 1px solid #e66643;\n"
"border-radius: 6px;\n"
"margin: 0;")
        self.NG.setObjectName("NG")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.NG)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.ng_image = QtWidgets.QLabel(self.NG)
        self.ng_image.setStyleSheet("color: #e66643;\n"
"border: none;\n"
"background-color: #00000000;")
        self.ng_image.setText("")
        self.ng_image.setAlignment(QtCore.Qt.AlignCenter)
        self.ng_image.setObjectName("ng_image")
        self.verticalLayout_5.addWidget(self.ng_image)
        self.NG_message_label = QtWidgets.QLabel(self.NG)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.NG_message_label.setFont(font)
        self.NG_message_label.setStyleSheet("margin: 4px 0;\n"
"color: #e66643;\n"
"border: none;\n"
"background-color: transparent;")
        self.NG_message_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.NG_message_label.setObjectName("NG_message_label")
        self.verticalLayout_5.addWidget(self.NG_message_label)
        self.ng_score = QtWidgets.QLabel(self.NG)
        self.ng_score.setStyleSheet("color: #aaaaaa;\n"
"background-color: #00000000;\n"
"border: none;")
        self.ng_score.setAlignment(QtCore.Qt.AlignCenter)
        self.ng_score.setObjectName("ng_score")
        self.verticalLayout_5.addWidget(self.ng_score)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.result.addWidget(self.NG)
        self.verticalLayout_2.addWidget(self.result)
        self.widget = QtWidgets.QWidget(inspection)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.counter = QtWidgets.QWidget(inspection)
        self.counter.setStyleSheet("background-color: #f5f5f5;\n"
"border: 1px solid #aaaaaa;\n"
"border-radius: 6px;\n"
"margin: 0;")
        self.counter.setObjectName("counter")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.counter)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.total_header_label = QtWidgets.QLabel(self.counter)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.total_header_label.setFont(font)
        self.total_header_label.setStyleSheet("color: #3e3e3e;\n"
"border:none;\n"
"")
        self.total_header_label.setObjectName("total_header_label")
        self.horizontalLayout_2.addWidget(self.total_header_label)
        self.OK_icon_label = QtWidgets.QLabel(self.counter)
        self.OK_icon_label.setStyleSheet("border:none;\n"
"")
        self.OK_icon_label.setText("")
        self.OK_icon_label.setPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_check-circle_32_4_3fda68_none.png"))
        self.OK_icon_label.setObjectName("OK_icon_label")
        self.horizontalLayout_2.addWidget(self.OK_icon_label)
        self.OK_counter_label = QtWidgets.QLabel(self.counter)
        self.OK_counter_label.setStyleSheet("color: #3FDA68;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"border:none;\n"
"")
        self.OK_counter_label.setText("")
        self.OK_counter_label.setScaledContents(False)
        self.OK_counter_label.setObjectName("OK_counter_label")
        self.horizontalLayout_2.addWidget(self.OK_counter_label)
        self.NG_icon_label = QtWidgets.QLabel(self.counter)
        self.NG_icon_label.setStyleSheet("border:none;\n"
"")
        self.NG_icon_label.setText("")
        self.NG_icon_label.setPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_times-circle_32_4_e66643_none.png"))
        self.NG_icon_label.setObjectName("NG_icon_label")
        self.horizontalLayout_2.addWidget(self.NG_icon_label)
        self.NG_counter_label = QtWidgets.QLabel(self.counter)
        self.NG_counter_label.setStyleSheet("color: #E66643;\n"
"font-weight: bold;\n"
"font-size: 14px;\n"
"border:none;\n"
"")
        self.NG_counter_label.setText("")
        self.NG_counter_label.setObjectName("NG_counter_label")
        self.horizontalLayout_2.addWidget(self.NG_counter_label)
        self.verticalLayout_2.addWidget(self.counter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem11)

        self.retranslateUi(inspection)
        self.result.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(inspection)

    def retranslateUi(self, inspection):
        _translate = QtCore.QCoreApplication.translate
        inspection.setWindowTitle(_translate("inspection", "Form"))
        self.select_camera_button.setText(_translate("inspection", "表示するカメラを選択"))
        self.inspect_button.setText(_translate("inspection", "撮影して判定"))
        self.default_label.setText(_translate("inspection", "ここに判定結果が<br/>表示されます。"))
        self.OK_message_label.setText(_translate("inspection", "この製品は良品です"))
        self.NG_message_label.setText(_translate("inspection", "この製品は不良品です"))
        self.ng_score.setText(_translate("inspection", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.total_header_label.setText(_translate("inspection", "累計"))


from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import icon_rc
