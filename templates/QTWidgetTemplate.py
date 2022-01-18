import sys
import os

from PySide2.QtWidgets import QApplication, QWidget,QMainWindow, QAction,QHeaderView , QFileDialog, QStackedWidget,QListView,QMessageBox,QLabel,QGraphicsScene
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QImage,  QPixmap
from PySide2.QtUiTools import QUiLoader
from Qt import QtCore, QtGui, QtWidgets
from shutil import copyfile
from PySide2.QtCore import Signal,QThread

from %FPATHDOT% import Ui_Form



class %FCLASSNAME%(QWidget):
    cameraCount = Signal(int)
    def __init__(self, parent = None,context = None,):
        super(%FCLASSNAME%, self).__init__()
        self.loaded = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.textSizeA.editingFinished.connect(self.textSizeAChanged)
        # self.ui.pushButton_StopProcess.clicked.connect(self.StopAIThread)
        # self.ui.pushButton_StartWebcam.clicked.connect(self.OpenWebcam)
        self.loaded = True
