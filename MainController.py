#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget
from VideoPlayer import VideoPlayer
from TrackerProcess import MainWindow
from MakePlot import MainPlotWindow
import sys
import os



class Ui_Frame(object):
    def setupUi(self, Frame, VWidget, TrackerWindow, PlotWindow):
        Frame.setObjectName("Frame")
        Frame.resize(1024, 864)
        self.gridLayoutWidget = QtWidgets.QWidget(Frame)
        #self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 60, 521, 301))
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 1000, 850))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        VWidget.setContentsMargins(0, 0, 0, 0)
        VWidget.setGeometry(QtCore.QRect(5, 5, 1024, 864))
        TrackerWindow.setGeometry(QtCore.QRect(5, 5, 500, 250))
        #self.gridLayout.addWidget(w, 2, 0, 1, 1)
        self.gridLayout.addWidget(VWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(TrackerWindow, 0, 0, 1, 1)
        self.gridLayout.addWidget(PlotWindow, 2, 0, 1, 1)


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Yolov4 Object Tracking"))



    def generatePathName(self, folder):
        #i = 0
        path_ = "./outputs"

        i =  int(''.join(filter(str.isdigit, folder)))
 
        while os.path.exists(path_ + "/" + folder + "/123output.avi"):
            i += 1
            folder = "%soutput" %i
        if os.path.exists(path_ + "/" + folder):
            if not os.path.exists(path_ + "/" + folder + "/123output.avi"):
                os.rmdir(path_ + "/" + folder)
        os.mkdir(path_ + "/" + folder)
        fFinal = path_ + "/" + folder

        return fFinal

    

        
def main():
    global app
    app = QApplication(sys.argv)
    window = MainWindow()
    Frame = QtWidgets.QFrame()
    player = VideoPlayer()
    ui = Ui_Frame()
    plot = MainPlotWindow()
    Frame.setFixedSize(1024,900)
    fileName = "123output.avi"
    folderName = "0output"
    pathName = ui.generatePathName(folderName)
    if pathName != "":
        finalFileName = pathName + "/" + fileName
    else:
        finalFileName = "./outputs/" + folderName + "/" + fileName


    cmd1 = "python save_model.py --model yolov4" 
    cmd2 = "python object_tracker.py --video ./data/video/project_video_2.mp4 --output"  + " " + finalFileName + " " + "--model yolov4 --dont_show --count --info"

    window.setFixedSize(1024, 300)

    if pathName != "":
        plotFileName = pathName + "/" + "info.txt"
    else:
        plotFileName = "./outputs/" + folderName + "/" + "info.txt"
     
    window.sendParams(cmd1, cmd2, app, finalFileName, plotFileName, player, plot)

    player.setFixedSize(1024, 664)
    ui.setupUi(Frame, player, window, plot)
    window.show()
    player.show()
    Frame.show()  
    plot.show()

    app.exec_()
    
    
if __name__ == '__main__':
    main()