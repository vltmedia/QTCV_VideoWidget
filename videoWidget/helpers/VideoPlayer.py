import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtCore import QUrl
from PySide2.QtMultimediaWidgets import QVideoWidget
from Qt import QtCore


class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parentobj = None, usePlaylist = True):
        super(VideoPlayer, self).__init__()
        self.parentobj = parentobj
        self.usePlaylist = usePlaylist
        self.playlist = None
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.videoPositionChanged)
        self.player.stateChanged.connect(self.videoStateChanged)
        # self.resize(QtCore.QSize(400, 300))
        self.file = ''  
        self.currentIndex = 0
        self.isPlaying = False
        self.FirstStart = False

    videoPositionChangedOut = QtCore.Signal(float)
    videoStopped = QtCore.Signal()
    videoPlaying = QtCore.Signal()

    def videoStateChanged(self, state_):
        if state_ == QMediaPlayer.State.StoppedState:
            self.videoPlaying.emit()

        if state_ == QMediaPlayer.State.PlayingState:
            self.videoStopped.emit()

    def videoPositionChanged(self, newpos):
        dur = 0
        if newpos != 0:
            try:
                dur = 100 * ( newpos / self.player.duration())
            except:
                dur = 0
        else:

            if self.FirstStart == True:
                self.FirstStart = False
            else:
                self.videoStopped.emit()

        self.videoPositionChangedOut.emit(dur)

    def GetPlayerPosition(self):
        cleaned = self.player.position() / self.player.duration()


    def ResizePlayer(self, size):
        # QtCore.QSize(400, 300)
        self.resize(size)
        
    def PlayVideoURL(self,url ="http://mirrors.standaloneinstaller.com/video-sample/star_trails.mp4" ):
        self.file = url
        self.FirstStart = True
        self.playlist = QMediaPlaylist(self.player)
        self.playlist.addMedia(QUrl(url))

        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)

        self.playlist.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.video_widget)
        self.setLayout(self.layout)
        self.isPlaying = True
        self.player.play()



    def PlayVideoFile(self,filepath ="http://mirrors.standaloneinstaller.com/video-sample/star_trails.mp4" ):
        if self.file != filepath:
            self.file = filepath
            self.FirstStart = True

            if self.playlist == None:
                self.currentIndex = 0
                self.playlist = QMediaPlaylist(self.player)
                self.playlist.addMedia(QUrl.fromLocalFile(filepath))

                self.video_widget = QVideoWidget()
                self.player.setVideoOutput(self.video_widget)
                self.playlist.setCurrentIndex(0)
                self.player.setPlaylist(self.playlist)

                self.layout = QtWidgets.QVBoxLayout()
                self.layout.addWidget(self.video_widget)
                self.setLayout(self.layout)
            else:
                addd = 0
                if self.usePlaylist:
                    addd = self.currentIndex + 1
                    self.currentIndex = addd
                else:
                    self.playlist.clear()
                self.playlist.addMedia(QUrl.fromLocalFile(filepath))
                self.playlist.setCurrentIndex(addd)
        self.isPlaying = True
        self.player.play()

    def LoadVideoFile(self,filepath ="http://mirrors.standaloneinstaller.com/video-sample/star_trails.mp4" ):
        self.file = filepath
        self.FirstStart = True
        if self.playlist == None:
            self.currentIndex = 0
            self.playlist = QMediaPlaylist(self.player)
            self.playlist.addMedia(QUrl.fromLocalFile(filepath))

            self.video_widget = QVideoWidget()
            self.player.setVideoOutput(self.video_widget)

            self.playlist.setCurrentIndex(0)
            self.player.setPlaylist(self.playlist)

            self.layout = QtWidgets.QVBoxLayout()
            self.layout.addWidget(self.video_widget)
            self.setLayout(self.layout)
        else:
            addd = self.currentIndex + 1
            self.currentIndex = addd

            self.playlist.addMedia(QUrl.fromLocalFile(filepath))
            self.playlist.setCurrentIndex(addd)

        self.player.stop()
        self.player.setPosition(1)

    def RestartVideo(self):
        self.player.setPosition(0)
        self.player.stop()
        self.isPlaying = True
        self.player.play()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.raise_()
    player.show()
    app.exec_()
