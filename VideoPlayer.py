#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication, QSlider, QLabel, QFileDialog, QStyle, QVBoxLayout, QHBoxLayout)
import sys


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
       # self.setWindowTitle("PyQt5 Video Player") 
 
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        self.playButton.setEnabled(False)
        
      
        
        self.stopButton = QPushButton()
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.clicked.connect(self.stop)
        self.stopButton.setEnabled(False)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.positionSlider.setEnabled(False)

        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.error.connect(self.handleError)
 
        #self.openButton = QPushButton("Open Video")   
        #self.openButton.clicked.connect(self.openFile)
 

        widget1 = QWidget(self)
        #self.setCentralWidget(widget1)
        #layout.addWidget(self.openButton)
        layout1 = QHBoxLayout()
        layout1.setContentsMargins(0,0,0,0)
        layout1.addWidget(self.playButton)
        layout1.addWidget(self.stopButton)
        layout1.addWidget(self.positionSlider)
        widget1.setLayout(layout1)

        
 
        widget2 = QWidget(self)
        self.setCentralWidget(widget2)
        layout2 = QVBoxLayout()
        layout2.setContentsMargins(0,0,0,0)
        layout2.addWidget(videoWidget)
        layout2.addWidget(widget1)
        widget2.setLayout(layout2)
        widget2.setGeometry(QtCore.QRect(0,0, 1024, 864))

      

        
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        
 
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
 
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            
            
    def playVideoFile(self, f):
        global fileName
        fileName = f
        if fileName != '':
                self.mediaPlayer.setMedia(
                        QMediaContent(QUrl.fromLocalFile(fileName))) 
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            
            
    def play(self):
        #if fileName != '':
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            
    """def pause(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()"""
            
    def stop(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.stop()
        """else:
            self.mediaPlayer.play()"""
        
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
  



      
    """def main():
        #global app
        #app = QApplication(sys.argv)
        #player = VideoPlayer()
        #VideoPlayer.playVideoFile(fileName)
        #app.exec_()
        #return app

    if __name__ == "__main__":
        main()"""

