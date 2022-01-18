import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow,QVBoxLayout, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene, QPushButton, QSlider, QStyle, QHBoxLayout, QStackedLayout
from PySide2.QtCore import QFile, QObject, Qt,  QDir, Qt, QUrl, QSize
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal, QThread
from PySide2.QtMultimediaWidgets import QVideoWidget

# from videoWidget.VideoWidget import VideoWidget
# from videoWidget.widgets.vidWidget_Widget import VideoWidget_ as VideoWidget
from videoWidget.VideoWidget import VideoWidget
# from MainWindow.form import Ui_main


class VideoWindow(QMainWindow):

    def __init__(self, parent=None, context=None, ):
        super(VideoWindow, self).__init__()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.VideoWidget = VideoWidget()
        self.setWindowTitle("Video Widget")

        # Create new action
        openAction = QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.VideoWidget.openFile)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(openAction)

        self.StackedWidget = QStackedLayout()
        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        layout = QVBoxLayout()
        layout.addLayout(self.StackedWidget)
        self.StackedWidget.addWidget(self.VideoWidget)
        self.StackedWidget.setCurrentIndex(0)
        # layout.addWidget(self.VideoWidget)

        # Set widget to contain window contents
        wid.setLayout(layout)


    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.VideoWidget.loadFile(fileName)



    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())