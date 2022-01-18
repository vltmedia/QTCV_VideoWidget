import sys
import os

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal, QThread
from videoWidget.VideoWidget import VideoWidget
from MainWindow.form import Ui_main
from videoWidget.VideoWidget import VideoWidget


class Ui_Main(QMainWindow):

    def __init__(self, parent=None, context=None, ):
        super(Ui_Main, self).__init__()
        self.VideoWidgetR = None
        self.VideoWidgetL = None
        self.loaded = False
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.VideoWidget = VideoWidget(self)
        self.VideoWidget2 = VideoWidget(self)
        self.ui.horizontalLayout.addWidget(self.VideoWidget)
        self.ui.horizontalLayout.addWidget(self.VideoWidget2)
        # self.Video_Window.show()
        # self.ui.stackedWidget.show()
        # self.SetupVideoWidget()
        # self.ui.textSizeA.editingFinished.connect(self.textSizeAChanged)
        self.ui.pushButton_LoadA.clicked.connect(self.LoadAVideo)
        # self.ui.pushButton_StartWebcam.clicked.connect(self.OpenWebcam)
        self.loaded = True

    def LoadAVideo(self):
        if os.path.exists(self.ui.lineEdit_VideoA.text()) :
            self.ui.widget.LoadVideoFile(self.ui.lineEdit_VideoA.text())

    def SetupVideoWidget(self):
        self.VideoWidgetL = VideoWidget(self)
        self.ui.horizontalLayout.addWidget(self.VideoWidgetL)
        self.VideoWidgetL.show()

        self.VideoWidgetR = VideoWidget(self)
        self.ui.horizontalLayout.addWidget(self.VideoWidgetR)
        self.VideoWidgetR.show()
