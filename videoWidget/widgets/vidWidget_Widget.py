import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow,QVBoxLayout, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene, QPushButton, QSlider, QStyle, QHBoxLayout, QStackedLayout, QTableView
from PySide2.QtCore import QFile, QObject, Qt,  QDir, Qt, QUrl, QSize
from PySide2.QtGui import QImage, QPixmap, QCursor, QIcon, QFont
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets,QRect
from shutil import copyfile
from PySide2.QtCore import Signal, QThread
from PySide2.QtMultimediaWidgets import QVideoWidget
from helpers.OpenCV.CV2VideoHandler import GetFrameFromVideoQPixmap, GetVideosInfo, GetFrameFromVideoNormalizedQPixmap,GetVideoInfo
from videoController.VideoController import VideoController
from videoWidget.VideoWidget import VideoWidget
# from MainWindow.form import Ui_main


class VideoWidget_(QWidget):

    def __init__(self, parent=None, context=None, ):
        super(VideoWidget_, self).__init__()
        self.InputVideoInfo = None
        self.CurrentMedia = None
        self.VController = VideoController(self)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.StackedWidget = QStackedLayout()

        videoWidget = QVideoWidget()

        # self.playButton = QPushButton()
        # self.playButton.setEnabled(False)
        # self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        # self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)


        self.graphicView_Entry = QLabel()
        self.graphicView_Entry.setObjectName(u"graphicView_Entry")
        self.graphicView_Entry.setMinimumSize(QSize(640, 360))
        self.graphicView_Entry.setMaximumSize(QSize(640, 360))
        self.graphicView_Entry.setPixmap(QPixmap(u":/media/images/placeholder/VideoNotFound169.png"))
        self.graphicView_Entry.setScaledContents(True)



        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        # controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        self.layout = QVBoxLayout()
        self.CurrentEntryTableView = QTableView()
        self.CurrentEntryTableView.setObjectName(u"CurrentEntryTableView")
        self.CurrentEntryTableView.setGeometry(QRect(20, 30, 1291, 381))
        self.VController.pushButton_PlayButton.clicked.connect(self.play)
        self.layout.addWidget(self.CurrentEntryTableView)
        self.layout.addLayout(self.StackedWidget)
        self.layout.addWidget(self.VController)

        self.layout.addLayout(controlLayout)
        # self.VideoController.setLayout(layout)
        self.StackedWidget.addWidget(videoWidget)
        self.StackedWidget.addWidget(self.graphicView_Entry)
        self.StackedWidget.setCurrentIndex(1)
        # Set widget to contain window contents
        self.setLayout(self.layout)

        self.player.setVideoOutput(videoWidget)
        self.player.stateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.error.connect(self.handleError)


    def UpdateTableView(self):
        self.InputVideoInfo = GetVideoInfo(self.CurrentMedia)
        self.ui.CurrentEntryTableView.setModel(self.InputVideoInfo["Model"])
        self.ui.CurrentEntryTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def loadFile(self, filePath):
        if os.path.exists(filePath):
            self.CurrentMedia = filePath
            self.player.setMedia(
                QMediaContent(QUrl.fromLocalFile(filePath)))
            # self.playButton.setEnabled(True)
            self.VController.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_Play.png"))
            # self.StackedWidget.setCurrentIndex(0)

            self.graphicView_Entry.setPixmap(GetFrameFromVideoQPixmap(filePath, 0))
            self.StackedWidget.setCurrentIndex(1)
            self.UpdateTableView()


    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())
        if fileName != '':
            self.loadFile(fileName)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()
            self.StackedWidget.setCurrentIndex(0)

    def mediaStateChanged(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.VController.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_62.png"))
            # self.playButton.setIcon(
            #     self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.VController.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_Play.png"))
            #
            # self.playButton.setIcon(
            #     self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        if self.player.state() != QMediaPlayer.PlayingState:
            self.player.setPosition(position)
            self.graphicView_Entry.setPixmap(GetFrameFromVideoNormalizedQPixmap(self.CurrentMedia, position / self.player.duration()))
            self.StackedWidget.setCurrentIndex(1)

    def handleError(self):
        # self.playButton.setEnabled(False)
        self.VController.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_Play.png"))

        self.errorLabel.setText("Error: " + self.player.errorString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())