# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoWidget_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(641, 453)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 642, 362))
        self.VidLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.VidLayout.setObjectName(u"VidLayout")
        self.VidLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.VidLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 642, 453))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setStyleSheet(u"font: 400 10pt \"Inter\";\n"
"color:#418ED6")

        self.verticalLayout.addWidget(self.label_4)

        self.graphicView_Entry = QLabel(self.verticalLayoutWidget_2)
        self.graphicView_Entry.setObjectName(u"graphicView_Entry")
        self.graphicView_Entry.setMinimumSize(QSize(640, 360))
        self.graphicView_Entry.setMaximumSize(QSize(640, 360))
        self.graphicView_Entry.setPixmap(QPixmap(u":/media/images/placeholder/VideoNotFound169.png"))
        self.graphicView_Entry.setScaledContents(True)

        self.verticalLayout.addWidget(self.graphicView_Entry)

        self.Slider_Video1 = QSlider(self.verticalLayoutWidget_2)
        self.Slider_Video1.setObjectName(u"Slider_Video1")
        self.Slider_Video1.setMaximum(100)
        self.Slider_Video1.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.Slider_Video1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_SeekBeginning = QPushButton(self.verticalLayoutWidget_2)
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

        self.horizontalLayout.addWidget(self.pushButton_SeekBeginning)

        self.pushButton_SeekL = QPushButton(self.verticalLayoutWidget_2)
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

        self.horizontalLayout.addWidget(self.pushButton_SeekL)

        self.pushButton_PlayButton = QPushButton(self.verticalLayoutWidget_2)
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

        self.horizontalLayout.addWidget(self.pushButton_PlayButton)

        self.pushButton_SeekR = QPushButton(self.verticalLayoutWidget_2)
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

        self.horizontalLayout.addWidget(self.pushButton_SeekR)

        self.pushButton_SeekEnd = QPushButton(self.verticalLayoutWidget_2)
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

        self.horizontalLayout.addWidget(self.pushButton_SeekEnd)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Viewer: Input", None))
        self.graphicView_Entry.setText("")
        self.pushButton_SeekBeginning.setText(QCoreApplication.translate("Form", u"|<", None))
        self.pushButton_SeekL.setText(QCoreApplication.translate("Form", u"<", None))
        self.pushButton_PlayButton.setText(QCoreApplication.translate("Form", u"Play", None))
        self.pushButton_SeekR.setText(QCoreApplication.translate("Form", u">", None))
        self.pushButton_SeekEnd.setText(QCoreApplication.translate("Form", u">|", None))
    # retranslateUi

