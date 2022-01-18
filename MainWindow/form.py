# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1686, 970)
        main.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 1621, 801))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 840, 641, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_VideoA = QLineEdit(self.widget)
        self.lineEdit_VideoA.setObjectName(u"lineEdit_VideoA")
        self.lineEdit_VideoA.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lineEdit_VideoA)

        self.pushButton_LoadA = QPushButton(self.widget)
        self.pushButton_LoadA.setObjectName(u"pushButton_LoadA")

        self.horizontalLayout_2.addWidget(self.pushButton_LoadA)

        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1686, 20))
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.lineEdit_VideoA.setText(QCoreApplication.translate("main", u"M:\\Projects\\Apps\\UAP_AI\\01-Working\\01-_User\\00-Source\\01-VIDZ\\Human\\yt\\Movies\\Random\\Gandalf_01.mp4", None))
        self.pushButton_LoadA.setText(QCoreApplication.translate("main", u"Load A", None))
    # retranslateUi

