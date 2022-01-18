import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QMainWindow,QVBoxLayout, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene, QPushButton, QSlider, QStyle, QHBoxLayout, QStackedLayout
from PySide2.QtCore import QFile, QObject, Qt,  QDir, Qt, QUrl, QSize
from PySide2.QtGui import QImage, QPixmap, QCursor, QIcon, QFont
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal,QThread

from videoController.videoController_ui import Ui_Form



class VideoFunctionsController(QWidget):
    cameraCount = Signal(int)
    def __init__(self, parent = None,context = None,):
        super(VideoFunctionsController, self).__init__()
        self.loaded = False
        self.resize(80, 40)
        self.setFixedHeight(40)
        self.setFixedWidth(80)
        self.controlLayoutB = QHBoxLayout(self)
        self.controlLayoutB.setContentsMargins(0, 0, 0, 0)
        self.CreateController()
        #
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        # self.ui.textSizeA.editingFinished.connect(self.textSizeAChanged)
        # self.ui.pushButton_StopProcess.clicked.connect(self.StopAIThread)
        # self.ui.pushButton_StartWebcam.clicked.connect(self.OpenWebcam)
        self.loaded = True
    def CreateController(self):

        font = QFont()
        font.setFamily(u"Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_OpenMedia = QPushButton(self)
        self.pushButton_OpenMedia.setObjectName(u"pushButton_SeekL")
        self.pushButton_OpenMedia.setMinimumSize(QSize(30, 30))
        self.pushButton_OpenMedia.setMaximumSize(QSize(30, 30))
        self.pushButton_OpenMedia.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_OpenMedia.setIcon(QIcon(u"://media/icons/app/icon_app_81.png"))
        self.pushButton_OpenMedia.setFont(font)
        self.pushButton_OpenMedia.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_OpenMedia.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_OpenMedia.setStyleSheet(u"\n"
                                                    "\n"
                                                    "background: #3A57E8;\n"
                                                    "border-radius: 4px;\n"
                                                    "font: 400 16px \"Poppins\";\n"
                                                    "\n"
                                                    "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_OpenMedia)

        self.pushButton_ScreenShot = QPushButton(self)
        self.pushButton_ScreenShot.setObjectName(u"pushButton_ScreenShot")
        self.pushButton_ScreenShot.setMinimumSize(QSize(30, 30))
        self.pushButton_ScreenShot.setMaximumSize(QSize(30, 30))
        self.pushButton_ScreenShot.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_ScreenShot.setFont(font)
        self.pushButton_ScreenShot.setIcon(QIcon(u"://media/icons/media/icon_media_28.png"))
        self.pushButton_ScreenShot.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_ScreenShot.setStyleSheet(u"\n"
                                              "\n"
                                              "background: #3A57E8;\n"
                                              "border-radius: 4px;\n"
                                              "font: 400 16px \"Poppins\";\n"
                                              "\n"
                                              "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_ScreenShot)
