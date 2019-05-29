# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Yusaku/仕事(ローカル)/RUTILEA/tazama/src/view/ui/startup.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartupWidget(object):
    def setupUi(self, StartupWidget):
        StartupWidget.setObjectName("StartupWidget")
        StartupWidget.setEnabled(True)
        StartupWidget.resize(520, 404)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartupWidget.sizePolicy().hasHeightForWidth())
        StartupWidget.setSizePolicy(sizePolicy)
        StartupWidget.setMinimumSize(QtCore.QSize(520, 404))
        StartupWidget.setMaximumSize(QtCore.QSize(520, 404))
        StartupWidget.setStyleSheet("QPushButton#new_project_button\n"
"{\n"
"   margin: 0 15 0 60;\n"
"   padding: 0 20;\n"
"   background-color: #3e3e3e;\n"
"   border: 1px solid #3e3e3e;\n"
"   border-radius:20px;\n"
"   color: #f5f5f5;\n"
"   font-weight: bold;\n"
"   font-size: 13px;\n"
"   height:40px;\n"
"}\n"
"\n"
"QPushButton#open_project_button\n"
"{\n"
"   margin: 0 60 0 15;\n"
"   padding: 0 20;\n"
"   background-color: #3e3e3e;\n"
"   border: 1px solid #666666;\n"
"   border-radius:20px;\n"
"   color: #f5f5f5;\n"
"   font-weight: bold;\n"
"   font-size: 13px;\n"
"   height:40px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed#new_project_button,\n"
"QPushButton:pressed#open_project_button\n"
"{\n"
"   background-color: #4298F9;\n"
"   border: 1px solid #4298F9;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(StartupWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.logo_icon_label = QtWidgets.QLabel(StartupWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_icon_label.sizePolicy().hasHeightForWidth())
        self.logo_icon_label.setSizePolicy(sizePolicy)
        self.logo_icon_label.setMaximumSize(QtCore.QSize(200, 47))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.logo_icon_label.setFont(font)
        self.logo_icon_label.setText("")
        self.logo_icon_label.setPixmap(QtGui.QPixmap(":/logo/assets/images/SDTest_logo.png"))
        self.logo_icon_label.setScaledContents(True)
        self.logo_icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_icon_label.setObjectName("logo_icon_label")
        self.horizontalLayout_2.addWidget(self.logo_icon_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_1.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.logo_title_label = QtWidgets.QLabel(StartupWidget)
        self.logo_title_label.setMaximumSize(QtCore.QSize(180, 28))
        self.logo_title_label.setStyleSheet("color: #3e3e3e;\n"
"font-size: 14px;\n"
"")
        self.logo_title_label.setObjectName("logo_title_label")
        self.horizontalLayout_3.addWidget(self.logo_title_label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_1.addLayout(self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(StartupWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label.setToolTipDuration(-1)
        self.label.setStyleSheet("color: #aaaaaa;\n"
"font-size: 14px;\n"
"")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_1.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_project_button = QtWidgets.QPushButton(StartupWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_project_button.sizePolicy().hasHeightForWidth())
        self.new_project_button.setSizePolicy(sizePolicy)
        self.new_project_button.setMinimumSize(QtCore.QSize(240, 0))
        self.new_project_button.setMaximumSize(QtCore.QSize(240, 16777215))
        self.new_project_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_plus_32_4_f5f5f5_none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_project_button.setIcon(icon)
        self.new_project_button.setIconSize(QtCore.QSize(16, 16))
        self.new_project_button.setCheckable(False)
        self.new_project_button.setChecked(False)
        self.new_project_button.setAutoRepeat(False)
        self.new_project_button.setAutoExclusive(False)
        self.new_project_button.setFlat(False)
        self.new_project_button.setObjectName("new_project_button")
        self.horizontalLayout.addWidget(self.new_project_button)
        self.open_project_button = QtWidgets.QPushButton(StartupWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_project_button.sizePolicy().hasHeightForWidth())
        self.open_project_button.setSizePolicy(sizePolicy)
        self.open_project_button.setMinimumSize(QtCore.QSize(240, 0))
        self.open_project_button.setMaximumSize(QtCore.QSize(240, 16777215))
        self.open_project_button.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/assets/fonts/fontawesome/font-awesome_4-7-0_file_32_4_f5f5f5_none.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_project_button.setIcon(icon1)
        self.open_project_button.setIconSize(QtCore.QSize(16, 16))
        self.open_project_button.setObjectName("open_project_button")
        self.horizontalLayout.addWidget(self.open_project_button)
        self.verticalLayout_1.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem6)

        self.retranslateUi(StartupWidget)
        QtCore.QMetaObject.connectSlotsByName(StartupWidget)
        StartupWidget.setTabOrder(self.new_project_button, self.open_project_button)

    def retranslateUi(self, StartupWidget):
        _translate = QtCore.QCoreApplication.translate
        StartupWidget.setWindowTitle(_translate("StartupWidget", "Form"))
        self.logo_title_label.setText(_translate("StartupWidget", "Software-Defined Test"))
        self.label.setText(_translate("StartupWidget", "Version 0.5"))
        self.new_project_button.setText(_translate("StartupWidget", "新規プロジェクト "))
        self.open_project_button.setText(_translate("StartupWidget", "開く"))


import icon_rc
import logo_rc
