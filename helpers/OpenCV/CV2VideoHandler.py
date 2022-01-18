import cv2
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QHeaderView, QFileDialog, QStackedWidget, \
    QListView, QMessageBox, QLabel, QGraphicsScene
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QImage, QPixmap, QStandardItemModel,QStandardItem
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtUiTools import QUiLoader
import os

def GetFrameFromVideoQPixmap(InputMedia, frame):
    cap = cv2.VideoCapture(InputMedia)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    cap.set(1, frame - 1)
    res, rgbOut = cap.read()
    height, width, channel = rgbOut.shape
    bytesPerLine = 3 * width
    qImg = QImage(rgbOut.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    cap.release()
    return QPixmap(qImg)


def GetFrameFromVideoNormalizedQPixmap(InputMedia, NormalizedNumber):
    cap = cv2.VideoCapture(InputMedia)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame = frame_count * NormalizedNumber
    if NormalizedNumber > 1.5:
        frame = frame_count * (NormalizedNumber / 100)
    if NormalizedNumber > 101:
        frame = 0
    duration = frame_count / fps
    cap.set(1, frame - 1)
    res, rgbOut = cap.read()
    height, width, channel = rgbOut.shape
    bytesPerLine = 3 * width
    qImg = QImage(rgbOut.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    cap.release()
    return QPixmap(qImg)


def GetFrameFromVideoAndSave(InputMedia, OutputFilePath, frame):
    cap = cv2.VideoCapture(InputMedia)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    cap.set(1, frame - 1)
    res, rgbOut = cap.read()
    cv2.imwrite(OutputFilePath, rgbOut)
    cap.release()
    return OutputFilePath


def GetVideoInfo(InputMedia):
    cap = cv2.VideoCapture(InputMedia)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    res, rgbOut = cap.read()
    cap.release()
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Media", "Framerate", "FrameCount", "Duration", "FullPath"])
    items = [
        QStandardItem(os.path.basename(InputMedia)), QStandardItem(str(fps)),QStandardItem(str(frame_count)),
        QStandardItem(str(duration)),QStandardItem(InputMedia)
    ]
    model.appendRow(items)
    return {
        "Media": InputMedia,
        "Framerate": fps,
        "FrameCount": frame_count,
        "Duration": duration,
        "Model": model
    }


def GetVideosInfo(InputMediaList):
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Media", "Framerate", "FrameCount", "Duration", "FullPath"])
    items = []
    OutJS = {"Entries": []}
    for InputMedia in InputMediaList:
        cap = cv2.VideoCapture(InputMedia)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        res, rgbOut = cap.read()
        cap.release()
        item = [
            QStandardItem(os.path.basename(InputMedia)), QStandardItem(str(fps)), QStandardItem(str(frame_count)),
            QStandardItem(str(duration)), QStandardItem(InputMedia)
        ]
        items.append(item)
        OutJS["Entries"].append({
            "Media": InputMedia,
            "Framerate": fps,
            "FrameCount": frame_count,
            "Duration": duration
        })
    model.appendRow(items)
    return {
        "Entries": OutJS["Entries"],
        "Model": model
    }

def GetVideoInfoUAISet(UAISet_):
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Media", "Framerate", "FrameCount", "Duration", "FullPath"])
    items = []
    OutJS = {"Entries": []}
    for entry in UAISet_.Entries:
        InputMedia = entry.url
        cap = cv2.VideoCapture(InputMedia)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        res, rgbOut = cap.read()
        cap.release()
        item = [
            QStandardItem(os.path.basename(InputMedia)), QStandardItem(str(fps)), QStandardItem(str(frame_count)),
            QStandardItem(str(duration)), QStandardItem(InputMedia)
        ]
        items.append(item)
        model.appendRow(item)
        OutJS["Entries"].append({
            "Media": InputMedia,
            "Framerate": fps,
            "FrameCount": frame_count,
            "Duration": duration
        })
    # model.appendRow(items)
    return {
        "Entries": OutJS["Entries"],
        "Model": model
    }
