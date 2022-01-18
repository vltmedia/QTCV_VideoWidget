import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow,QVBoxLayout, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene, QPushButton, QSlider,QTableView, QStyle, QHBoxLayout, QLineEdit ,QStackedLayout
from PySide2.QtCore import QFile, QObject, Qt,  QDir, Qt, QUrl, QSize,QRect

from PySide2.QtGui import QImage, QPixmap, QCursor, QIcon, QFont, QStandardItemModel,QStandardItem
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal, QThread
from PySide2.QtMultimediaWidgets import QVideoWidget
from helpers.OpenCV.CV2VideoHandler import GetFrameFromVideoQPixmap, GetVideosInfo, GetFrameFromVideoNormalizedQPixmap, \
    GetVideoInfo, GetFrameFromVideoAndSave
from videoController.VideoController import VideoController
from videoFunctionsController.VideoFunctionsController import VideoFunctionsController
# from videoWidget.VideoWidget import VideoWidget
# from MainWindow.form import Ui_main
import resources_rc


class VideoWidget(QWidget):

    def __init__(self, parent=None, context=None, ):
        super(VideoWidget, self).__init__()
        self.setMaximumSize(QSize(680, 550))
        self.CurrentFrame = 0
        self.lastDirectoryScreenshot = "/"
        self.CurrentMedia = None
        self.SetupUI()
        self.SetupPlayerConnections()


    def SetupUI(self):
        self.VController = VideoController(self)
        self.VideoFunctionsController = VideoFunctionsController(self)
        self.SetupController()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.StackedWidget = QStackedLayout()
        self.videoWidget = QVideoWidget()
        self.SetupFrameNumberLabel()
        self.SetupTimecodeNumberLabel()

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
        controlLayout.addLayout(self.FrameNumberLayout)
        controlLayout.addLayout(self.TimecodeNumberLayout)
        # Create layouts to place inside widget
        controlLayoutb = QHBoxLayout()
        controlLayoutb.setContentsMargins(0, 0, 0, 0)
        # controlLayout.addWidget(self.playButton)
        controlLayoutb.addWidget(self.VController)
        controlLayoutb.addWidget(self.VideoFunctionsController)

        self.layout = QVBoxLayout()
        self.CurrentEntryTableView = QTableView()
        self.CurrentEntryTableView.setObjectName(u"CurrentEntryTableView")
        self.CurrentEntryTableView.setGeometry(QRect(20, 20, 20, 20))
        self.CurrentEntryTableView.setModel(self.CreateEmptyEntry())
        self.VController.pushButton_PlayButton.clicked.connect(self.play)
        self.layout.addWidget(self.CurrentEntryTableView)
        self.layout.addLayout(self.StackedWidget)
        self.layout.addLayout(controlLayout)
        self.layout.addLayout(controlLayoutb)
        # self.layout.addWidget(self.VController)

        # self.VideoController.setLayout(layout)
        self.StackedWidget.addWidget(self.videoWidget)
        self.StackedWidget.addWidget(self.graphicView_Entry)
        self.StackedWidget.setCurrentIndex(1)
        # Set widget to contain window contents
        self.setLayout(self.layout)

    def SetupController(self):
        self.VController.pushButton_SeekR.clicked.connect(self.NextFrame)
        self.VController.pushButton_SeekL.clicked.connect(self.PrevFrame)
        self.VController.pushButton_SeekEnd.clicked.connect(self.LastFrame)
        self.VController.pushButton_SeekBeginning.clicked.connect(self.FirstFrame)
        self.VideoFunctionsController.pushButton_ScreenShot.clicked.connect(self.ScreenShot)
        self.VideoFunctionsController.pushButton_OpenMedia.clicked.connect(self.openFile)

    def SetupFrameNumberLabel(self):
        self.TitleFrameLabel = QLabel()
        self.TitleFrameLabel.setText("Frame:")
        self.TitleFrameLabel.setObjectName(u"TitleFrameLabel")
        self.TitleFrameLabel.setMinimumSize(QSize(38, 20))
        self.TitleFrameLabel.setMaximumSize(QSize(38, 20))
        self.FrameNumberLabel = QLineEdit()
        self.FrameNumberLabel.editingFinished.connect(self.FrameChanged)
        self.FrameNumberLabel.setObjectName(u"FrameNumberLabel")
        self.FrameNumberLabel.setText("0")
        self.FrameNumberLabel.setMinimumSize(QSize(40, 20))
        self.FrameNumberLabel.setMaximumSize(QSize(40, 20))
        self.SepperatorFrameLabel = QLabel()
        self.SepperatorFrameLabel.setText("/")
        self.SepperatorFrameLabel.setObjectName(u"SepperatorFrameLabel")
        self.SepperatorFrameLabel.setMinimumSize(QSize(20, 20))
        self.SepperatorFrameLabel.setMaximumSize(QSize(20, 20))
        self.DurationNumberLabel = QLabel()
        self.DurationNumberLabel .setText("0")
        self.DurationNumberLabel.setObjectName(u"DurationNumberLabel")
        self.DurationNumberLabel.setMinimumSize(QSize(40, 20))
        self.DurationNumberLabel.setMaximumSize(QSize(40, 20))
        self.FrameNumberLayout = QHBoxLayout()
        self.FrameNumberLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameNumberLayout.addWidget(self.TitleFrameLabel)
        self.FrameNumberLayout.addWidget(self.FrameNumberLabel)
        self.FrameNumberLayout.addWidget(self.SepperatorFrameLabel)
        self.FrameNumberLayout.addWidget(self.DurationNumberLabel)

    def SetupTimecodeNumberLabel(self):
        self.TitleTimecodeLabel = QLabel()
        self.TitleTimecodeLabel.setText("Timecode:")
        self.TitleTimecodeLabel.setObjectName(u"TitleTimecodeLabel")
        self.TitleTimecodeLabel.setMinimumSize(QSize(60, 20))
        self.TitleTimecodeLabel.setMaximumSize(QSize(60, 20))
        self.TimecodeNumberLabel = QLabel()
        self.TimecodeNumberLabel.setObjectName(u"TimecodeNumberLabel")
        self.TimecodeNumberLabel.setText(self.frames_to_TC(0, 24))
        self.TimecodeNumberLabel.setMinimumSize(QSize(70, 20))
        self.TimecodeNumberLabel.setMaximumSize(QSize(70, 20))
        self.SepperatorTimecodeLabel = QLabel()
        self.SepperatorTimecodeLabel.setText("/")
        self.SepperatorTimecodeLabel.setObjectName(u"SepperatorTimecodeLabel")
        self.SepperatorTimecodeLabel.setMinimumSize(QSize(10, 20))
        self.SepperatorTimecodeLabel.setMaximumSize(QSize(10, 20))
        self.TimecodeDurationNumberLabel = QLabel()
        self.TimecodeDurationNumberLabel .setText("0")
        self.TimecodeDurationNumberLabel.setObjectName(u"DurationNumberLabel")
        self.TimecodeDurationNumberLabel.setMinimumSize(QSize(70, 20))
        self.TimecodeDurationNumberLabel.setMaximumSize(QSize(70, 20))
        self.TimecodeDurationNumberLabel.setText(self.frames_to_TC(0, 24))
        self.TimecodeNumberLayout = QHBoxLayout()
        self.TimecodeNumberLayout.setContentsMargins(0, 0, 0, 0)
        self.TimecodeNumberLayout.addWidget(self.TitleTimecodeLabel)
        self.TimecodeNumberLayout.addWidget(self.TimecodeNumberLabel)
        self.TimecodeNumberLayout.addWidget(self.SepperatorTimecodeLabel)
        self.TimecodeNumberLayout.addWidget(self.TimecodeDurationNumberLabel)


    def FrameChanged(self):
        num = float(self.FrameNumberLabel.text())
        if num <= self.InputVideoInfo['FrameCount']:
            normaled = num / float(self.InputVideoInfo['FrameCount'])
            newPos = (self.player.duration() * normaled) + 1
            self.setPosition(newPos)
            print(newPos)
        else:
            self.FrameNumberLabel.setText(0)
            self.setPosition(0)

    def SetupPlayerConnections(self):
        self.player.setVideoOutput(self.videoWidget)
        self.player.stateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.error.connect(self.handleError)

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

    def UpdateTableView(self):
        self.InputVideoInfo = GetVideoInfo(self.CurrentMedia)
        self.DurationNumberLabel.setText(str(self.InputVideoInfo['FrameCount']))
        self.CurrentEntryTableView.setModel(self.InputVideoInfo["Model"])
        self.CurrentEntryTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def CreateEmptyEntry(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Media", "Framerate", "FrameCount", "Duration", "FullPath"])
        items = [
            QStandardItem("N/A"), QStandardItem("N/A"), QStandardItem("N/A"),
            QStandardItem("N/A"), QStandardItem("N/A")
        ]
        model.appendRow(items)
        return model


    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, self.lastDirectoryScreenshot,"Open Movie","Videos (*.mp4 *.mov *.avi);;All (*)")
        if fileName != '':
            self.lastDirectoryScreenshot = os.path.dirname(fileName)
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
        frame = 0
        if position != 0:
            frame = (position / self.player.duration()) * self.InputVideoInfo['FrameCount']
        self.FrameNumberLabel.setText(str(int(frame)))
        self.CurrentFrame = frame
        timecodeDuration = self.frames_to_TC(0, 24)
        timecodeCurrent = self.frames_to_TC(0, 24)
        try:
            timecodeDuration = self.frames_to_TC(self.InputVideoInfo['FrameCount'], int(self.InputVideoInfo['Framerate']))
            timecodeCurrent = self.frames_to_TC(frames=frame, frameRate=int(self.InputVideoInfo['Framerate']))
        except:
            pass
        self.TimecodeNumberLabel.setText(timecodeCurrent)


    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
        self.DurationNumberLabel.setText(str(self.InputVideoInfo['FrameCount']))
        timecodeDuration = self.frames_to_TC(0, 24)
        try:
            timecodeDuration = self.frames_to_TC(self.InputVideoInfo['FrameCount'],
                                                 int(self.InputVideoInfo['Framerate']))
        except:
            pass
        self.TimecodeDurationNumberLabel.setText(timecodeDuration)

    def NextFrame(self):
        nextFrame = self.CurrentFrame + 1
        nextPos = float(self.player.duration()) * (float(nextFrame) / float(self.InputVideoInfo['FrameCount']))
        if nextPos < self.player.duration() + 1:
            self.setPosition(nextPos)

    def PrevFrame(self):
        nextFrame = self.CurrentFrame - 1
        nextPos = float(self.player.duration()) * (float(nextFrame) / float(self.InputVideoInfo['FrameCount']))
        if nextFrame > 0:
            self.setPosition(nextPos)

    def LastFrame(self):
        nextPos = float(self.player.duration()) * 0.9999
        self.setPosition(nextPos )

    def FirstFrame(self):
        self.setPosition(0 )

    def GetCurrentFrame(self):
        return self.CurrentFrame

    def ScreenShot(self):
        filename = QFileDialog.getSaveFileName(self, "Save Frame", self.lastDirectoryScreenshot, "Images (*.png)")
        if filename:
            self.lastDirectoryScreenshot = os.path.dirname(filename[0])
            GetFrameFromVideoAndSave(self.CurrentMedia, filename[0],  self.CurrentFrame )

    def setPosition(self, position):
        if self.player.state() != QMediaPlayer.PlayingState:
            self.player.setPosition(position)
            normalized_ = position / self.player.duration()
            frame = normalized_ * self.InputVideoInfo['FrameCount']
            self.CurrentFrame = frame
            self.graphicView_Entry.setPixmap(GetFrameFromVideoNormalizedQPixmap(self.CurrentMedia, position / self.player.duration()))
            self.StackedWidget.setCurrentIndex(1)
            self.FrameNumberLabel.setText(str(int(frame)))
            self.TimecodeNumberLabel.setText(self.frames_to_TC(frames=frame, frameRate=int(self.InputVideoInfo['Framerate'])))

    def handleError(self):
        # self.playButton.setEnabled(False)
        self.VController.pushButton_PlayButton.setIcon(QIcon(u"://media/icons/media/icon_media_Play.png"))

        self.errorLabel.setText("Error: " + self.player.errorString())

    def frames_to_TC(self, frames, frameRate):
        h = int(frames / 86400)
        m = int(frames / 1440) % 60
        s = int((frames % 1440) / frameRate)
        f = frames % 1440 % frameRate
        return ("%02d:%02d:%02d:%02d" % (h, m, s, f))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())