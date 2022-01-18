# Description

A Video Widget powered by QT and OpenCV (for frame processing)

# Requirements

- Pyside2

- PyQT5

- OpenCV2

# Usage
## Add Widget
```py
from QTCV_VideoWidget.videoWidget.VideoWidget import VideoWidget
self.VideoWidget = VideoWidget(self)
self.ui.horizontalLayout.addWidget(self.VideoWidget)
```
## Load File
```py
self.VideoWidget.loadFile('C:/temp/yt/file01.mp4')
```
## Connect to Signals
```py
self.VideoWidget.PositionChanged.connect(self.PositionChanged)
self.VideoWidget.SliderPositionChanged.connect(self.SliderPositionChanged)
self.VideoWidget.StateChanged.connect(self.StateChanged)
```





![l](media/images/screenshots/QTVideoWidget_Base.png)

![l](media/images/screenshots/QTVideoWidget_WithVideo.png)
