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




class VideoController(QWidget):
    cameraCount = Signal(int)
    def __init__(self, parent = None,context = None,):
        super(VideoController, self).__init__()
        self.loaded = False
        self.resize(230, 40)
        self.setFixedHeight(40)
        self.setFixedWidth(190)
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

        self.pushButton_SeekBeginning = QPushButton(self)
        self.pushButton_SeekBeginning.setObjectName(u"pushButton_SeekBeginning")
        self.pushButton_SeekBeginning.setMinimumSize(QSize(30, 30))
        self.pushButton_SeekBeginning.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)


        self.pushButton_SeekBeginning.setIcon(QIcon(u"://media/icons/media/icon_media_65.png"))
        self.pushButton_SeekBeginning.setFont(font)
        self.pushButton_SeekBeginning.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_SeekBeginning.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekBeginning.setStyleSheet(u"\n"
                                                    "\n"
                                                    "background: #3A57E8;\n"
                                                    "border-radius: 4px;\n"
                                                    "font: 400 16px \"Poppins\";\n"
                                                    "\n"
                                                    "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_SeekBeginning)

        self.pushButton_SeekL = QPushButton(self)
        self.pushButton_SeekL.setObjectName(u"pushButton_SeekL")
        self.pushButton_SeekL.setMinimumSize(QSize(30, 30))
        self.pushButton_SeekL.setMaximumSize(QSize(30, 30))
        self.pushButton_SeekL.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_SeekL.setFont(font)
        self.pushButton_SeekL.setIcon(QIcon(u"://media/icons/media/icon_media_61.png"))
        self.pushButton_SeekL.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekL.setStyleSheet(u"\n"
                                            "\n"
                                            "background: #3A57E8;\n"
                                            "border-radius: 4px;\n"
                                            "font: 400 16px \"Poppins\";\n"
                                            "\n"
                                            "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_SeekL)

        self.pushButton_PlayButton = QPushButton(self)
        self.pushButton_PlayButton.setObjectName(u"pushButton_PlayButton")
        self.pushButton_PlayButton.setMinimumSize(QSize(30, 30))
        self.pushButton_PlayButton.setMaximumSize(QSize(30, 30))
        self.pushButton_PlayButton.setFont(font)
        self.pushButton_PlayButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_PlayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_PlayButton.setStyleSheet(u"\n"
                                                 "\n"
                                                 "background: #3A57E8;\n"
                                                 "border-radius: 4px;\n"
                                                 "font: 400 16px \"Poppins\";\n"
                                                 "\n"
                                                 "color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"://media/icons/media/icon_media_Play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_Play.png"))

        self.controlLayoutB.addWidget(self.pushButton_PlayButton)

        self.pushButton_SeekR = QPushButton(self)
        self.pushButton_SeekR.setObjectName(u"pushButton_SeekR")
        self.pushButton_SeekR.setMinimumSize(QSize(30, 30))
        self.pushButton_SeekR.setMaximumSize(QSize(30, 30))
        self.pushButton_SeekR.setIcon(QIcon(u"://media/icons/media/icon_media_60.png"))
        self.pushButton_SeekR.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_SeekR.setFont(font)
        self.pushButton_SeekR.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekR.setStyleSheet(u"\n"
                                            "\n"
                                            "background: #3A57E8;\n"
                                            "border-radius: 4px;\n"
                                            "font: 400 16px \"Poppins\";\n"
                                            "\n"
                                            "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_SeekR)

        self.pushButton_SeekEnd = QPushButton(self)
        self.pushButton_SeekEnd.setObjectName(u"pushButton_SeekEnd")
        self.pushButton_SeekEnd.setMinimumSize(QSize(30, 30))
        self.pushButton_SeekEnd.setMaximumSize(QSize(30, 30))
        self.pushButton_SeekEnd.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_SeekEnd.setFont(font)
        self.pushButton_SeekEnd.setIcon(QIcon(u"://media/icons/media/icon_media_64.png"))
        self.pushButton_SeekEnd.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_SeekEnd.setStyleSheet(u"\n"
                                              "\n"
                                              "background: #3A57E8;\n"
                                              "border-radius: 4px;\n"
                                              "font: 400 16px \"Poppins\";\n"
                                              "\n"
                                              "color: rgb(255, 255, 255);")

        self.controlLayoutB.addWidget(self.pushButton_SeekEnd)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoController()
    # player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())