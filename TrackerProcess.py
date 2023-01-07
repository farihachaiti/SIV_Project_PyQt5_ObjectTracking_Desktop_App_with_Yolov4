import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QHBoxLayout, QWidget, QProgressBar, QFileDialog)
from PyQt5.QtCore import QDir, QProcess, QTimer
import sys
import re
import os
import time
import progressbar
import asyncio
#from VideoPlayer import VideoPlayer
#import MainController


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None
        self.path = ""
        self.command2 = ""

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        
        self.btn_one = QPushButton("Execute Step 1")
        self.btn_one.pressed.connect(self.start_process_one)

        
        self.btn_two = QPushButton("Execute Step 2")
        self.btn_two.pressed.connect(self.start_process_two)

        self.progress_bar = QProgressBar(self)
  
        # setting its geometry
        self.progress_bar.setGeometry(30, 40, 200, 25)
        self.progress_bar.setStyleSheet("QProgressBar{ border: solid grey; border-width: 6; border-radius: 12px; color: black; text-align: centre; margin-right: 12; }, QProgressBar::chunk:vertical {background-color: #05B8CC; width: 20px;}")
        #self.progress_bar.setRange(0, 721)
        self.btn_three = QPushButton("Play Output Video")
      

        self.open_button = QPushButton(self)
        rMyIcon = QtGui.QPixmap("upload.png")
        self.open_button.setIcon(QtGui.QIcon(rMyIcon))
        self.open_button.clicked.connect(self.open)

        #global l
        l = QHBoxLayout()
        l.addWidget(self.open_button)
        l.addWidget(self.btn_one)
        l.addWidget(self.btn_two)        
        l.addWidget(self.progress_bar)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)
        

    def open(self):
        filter = "mp4(*.mp4)"
        self.path = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, "Open Video File", QDir.homePath(), filter)[0]
        if self.path:
            self.command2 = "python object_tracker.py --video" + " " + self.path + " " + "--output"  + " " + fileName + " " + "--model yolov4 --dont_show --count --info"
        print(command2)
        print(self.command2)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process_one(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start(command1)
          
        
    def start_process_two(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            if self.path:
                self.command2 = "python object_tracker.py --video" + " " + self.path + " " + "--output"  + " " + fileName + " " + "--model yolov4 --dont_show --count --info"
            else:
                self.command2 = command2
            print(self.command2+"after")
            self.p.start(self.command2)
            print(self.command2+"after")

    def stop(self):
        loop = asyncio.get_event_loop()
        loop.stop()
        self.destroy()
        self.hide()
        self.thread = None
        QTimer.singleShot(0, self.close)
        
            
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        self.message(stderr)

        
    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.job()
        self.message(stdout)

        
    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")
        

    def process_finished(self):
        self.message("Process finished.")
        self.p = None   
        if os.path.exists(fileName):
            VPlayer.playButton.setEnabled(True)
            VPlayer.stopButton.setEnabled(True)
            VPlayer.playButton.setEnabled(True)
            VPlayer.playVideoFile(fileName)
            VPlayer.show()
        if os.path.exists(plotFilename):
            Plot.sendFilePath(plotFilename, pathName)
            Plot.btn_plot.setEnabled(True)
            Plot.show()
        
        
    def job(self):
    #bar = progressbar.ProgressBar()
        for i in range(101):
  
            # slowing down the loop
            time.sleep(1.0)
  
            # setting value to progress bar
            self.progress_bar.setValue(i)
        
        

    def sendParams(self, cmd1, cmd2, a, f, p, player, plt, pname):
        global command1, command2, app, fileName, VPlayer, Plot, plotFilename, pathName
        command1 = cmd1
        if self.path:
                command2 = "python object_tracker.py --video" + " " + self.path + " " + "--output"  + " " + fileName + " " + "--model yolov4 --dont_show --count --info"
        else:
                command2 = cmd2
        app = a
        fileName = f
        plotFilename = p
        VPlayer = player
        Plot = plt
        pathName = pname
