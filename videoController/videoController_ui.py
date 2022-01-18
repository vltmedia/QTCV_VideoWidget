# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoController_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(331, 45)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 331, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_SeekBeginning = QPushButton(self.layoutWidget)
        self.pushButton_SeekBeginning.setObjectName(u"pushButton_SeekBeginning")
        self.pushButton_SeekBeginning.setMinimumSize(QSize(10, 40))
        self.pushButton_SeekBeginning.setMaximumSize(QSize(40, 16777215))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_SeekBeginning.setFont(font)
        self.pushButton_SeekBeginning.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekBeginning.setStyleSheet(u"\n"
"\n"
"background: #3A57E8;\n"
"border-radius: 4px;\n"
"font: 400 16px \"Poppins\";\n"
"\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_SeekBeginning)

        self.pushButton_SeekL = QPushButton(self.layoutWidget)
        self.pushButton_SeekL.setObjectName(u"pushButton_SeekL")
        self.pushButton_SeekL.setMinimumSize(QSize(20, 40))
        self.pushButton_SeekL.setMaximumSize(QSize(40, 16777215))
        self.pushButton_SeekL.setFont(font)
        self.pushButton_SeekL.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekL.setStyleSheet(u"\n"
"\n"
"background: #3A57E8;\n"
"border-radius: 4px;\n"
"font: 400 16px \"Poppins\";\n"
"\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_SeekL)

        self.pushButton_PlayButton = QPushButton(self.layoutWidget)
        self.pushButton_PlayButton.setObjectName(u"pushButton_PlayButton")
        self.pushButton_PlayButton.setMinimumSize(QSize(124, 40))
        self.pushButton_PlayButton.setMaximumSize(QSize(111, 16777215))
        self.pushButton_PlayButton.setFont(font)
        self.pushButton_PlayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_PlayButton.setStyleSheet(u"\n"
"\n"
"background: #3A57E8;\n"
"border-radius: 4px;\n"
"font: 400 16px \"Poppins\";\n"
"\n"
"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"://media/icons/media/icon_media_80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_PlayButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton_PlayButton)

        self.pushButton_SeekR = QPushButton(self.layoutWidget)
        self.pushButton_SeekR.setObjectName(u"pushButton_SeekR")
        self.pushButton_SeekR.setMinimumSize(QSize(10, 40))
        self.pushButton_SeekR.setMaximumSize(QSize(40, 16777215))
        self.pushButton_SeekR.setFont(font)
        self.pushButton_SeekR.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekR.setStyleSheet(u"\n"
"\n"
"background: #3A57E8;\n"
"border-radius: 4px;\n"
"font: 400 16px \"Poppins\";\n"
"\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_SeekR)

        self.pushButton_SeekEnd = QPushButton(self.layoutWidget)
        self.pushButton_SeekEnd.setObjectName(u"pushButton_SeekEnd")
        self.pushButton_SeekEnd.setMinimumSize(QSize(10, 40))
        self.pushButton_SeekEnd.setMaximumSize(QSize(40, 16777215))
        self.pushButton_SeekEnd.setFont(font)
        self.pushButton_SeekEnd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekEnd.setStyleSheet(u"\n"
"\n"
"background: #3A57E8;\n"
"border-radius: 4px;\n"
"font: 400 16px \"Poppins\";\n"
"\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_SeekEnd)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_SeekBeginning.setText(QCoreApplication.translate("Form", u"|<", None))
        self.pushButton_SeekL.setText(QCoreApplication.translate("Form", u"<", None))
        self.pushButton_PlayButton.setText(QCoreApplication.translate("Form", u"Play", None))
        self.pushButton_SeekR.setText(QCoreApplication.translate("Form", u">", None))
        self.pushButton_SeekEnd.setText(QCoreApplication.translate("Form", u">|", None))
    # retranslateUi

