# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from videoWidget.VideoWidget import VideoWidget
from MainWindow.form_widget import Ui_Main

if __name__ == "__main__":
    app = QApplication([])
    widget = Ui_Main()
    widget.show()
    sys.exit(app.exec_())
