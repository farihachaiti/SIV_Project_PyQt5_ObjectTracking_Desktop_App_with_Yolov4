from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.exporters
import sys  # We need sys so that we can pass argv to QApplication
import os
import random
import numpy as np

class Window2(QtWidgets.QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trajectory of Tracked Objects")
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


    def plotTrajectory(self, filePath):

        fl = open(filePath, 'r')
        data = fl.readlines()
        fl.close()


        
        #self.setCentralWidget(self.graphWidget)
        #self.graphWidget.setBackground('w')
        
        self.graphWidget.setTitle("Trajectory of Tracked Objects", color="b", size="25pt")

        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, 15, padding=0)
        self.graphWidget.setYRange(0, 15, padding=0)

        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "y: (°)", **styles)
        self.graphWidget.setLabel("bottom", "x: (°)", **styles)

        self.graphPlot(data)


        # save to file
        exporter = pg.exporters.ImageExporter( self.graphWidget.scene() )
        exporter.parameters()['width'] = 2000   # (note this also affects height parameter)
        exporter.export(filePath + 'trajectory.png')






    def get_color_name(self, rgb):
        colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "magenta": (255, 0, 255),
            "cyan": (0, 255, 255),
            "black": (0, 0, 0),
            "white": (255, 255, 255)
        }
        min_distance = float("inf")
        closest_color = None
        for color, value in colors.items():
            distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
            if distance < min_distance:
                min_distance = distance
                closest_color = color
        return closest_color


    def graphPlot(self, data):
        X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6, X7, Y7, X8, Y8, X9, Y9, X10, Y10, X11, Y11, X12, Y12, X13, Y13, X14, Y14, X15, Y15, X16, Y16, X17, Y17, X18, Y18, X19, Y19, X20, Y20, X21, Y21 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        

        for dt in data:
            dt2 = dt.split(',')
            frame, time, tracker_id, class_, xmin, ymin, xmax, ymax, x, y =  dt2
            tid = int(''.join(filter(str.isdigit, tracker_id)))
            #Tracks.append(tid)
            if tid == 1:
                #print(dt2) 
                x1 = float(''.join(filter(str.isdigit, x)))
                y1 = float(''.join(filter(str.isdigit, y)))
                x2 = x1/1000
                y2 = y1/1000
                X1.append(x2)
                Y1.append(y2)

            if tid == 2:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X2.append(x2)
                Y2.append(y2)

            if tid == 3:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X3.append(x2)
                Y3.append(y2)

            if tid == 4:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X4.append(x2)
                Y4.append(y2)

            if tid == 5:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X5.append(x2)
                Y5.append(y2)

            if tid == 10:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X6.append(x2)
                Y6.append(y2)
            
            if tid == 11:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X7.append(x2)
                Y7.append(y2)
        
            if tid == 13:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X8.append(x2)
                Y8.append(y2)

            if tid == 14:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X9.append(x2)
                Y9.append(y2)

            if tid == 15:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X10.append(x2)
                Y10.append(y2)

            if tid == 17:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X11.append(x2)
                Y11.append(y2)

            if tid == 19:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X12.append(x2)
                Y12.append(y2)

            if tid == 20:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X13.append(x2)
                Y13.append(y2)

            if tid == 21:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X14.append(x2)
                Y14.append(y2)

            if tid == 22:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X15.append(x2)
                Y15.append(y2)

            if tid == 25:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X16.append(x2)
                Y16.append(y2)

            if tid == 28:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X17.append(x2)
                Y17.append(y2)

            if tid == 29:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X18.append(x2)
                Y18.append(y2)

            if tid == 30:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X19.append(x2)
                Y19.append(y2)

            if tid == 31:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X20.append(x2)
                Y20.append(y2)

            if tid == 32:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X21.append(x2)
                Y21.append(y2)


        self.plot(X1, Y1, "Tracker ID: 1", 'y')
        self.plot(X2, Y2, "Tracker ID: 2", 'm')
        self.plot(X3, Y3, "Tracker ID: 3", 'w')
        self.plot(X4, Y4, "Tracker ID: 4", 'l')
        self.plot(X5, Y5, "Tracker ID: 5", 'b')
        self.plot(X6, Y6, "Tracker ID: 10", 'g')
        self.plot(X7, Y7, "Tracker ID: 11", 'r')
        self.plot(X8, Y8, "Tracker ID: 13", 'b')
        self.plot(X9, Y9, "Tracker ID: 14", 'g')
        self.plot(X10, Y10, "Tracker ID: 15", 'l')
        self.plot(X11, Y11, "Tracker ID: 17", 'd')
        self.plot(X12, Y12, "Tracker ID: 19", 'c')
        self.plot(X13, Y13, "Tracker ID: 20", 'r')
        self.plot(X14, Y14, "Tracker ID: 21", 'm')
        self.plot(X15, Y15, "Tracker ID: 22", 'w')
        self.plot(X16, Y16, "Tracker ID: 25", 'y')
        self.plot(X17, Y17, "Tracker ID: 28", 'r')
        self.plot(X18, Y18, "Tracker ID: 29", 'g')
        self.plot(X19, Y19, "Tracker ID: 30", 'w')
        self.plot(X20, Y20, "Tracker ID: 31", 'b')
        self.plot(X21, Y21, "Tracker ID: 32", 'r')

        

        
        # t = (np.unique(Tracks))
        # print(t)


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen)

class MainPlotWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.btn_plot = QtWidgets.QPushButton("Draw Trajectory of Tracked Objects")
        self.btn_plot.setMaximumSize(500, 50)
        self.btn_plot.pressed.connect(self.window2)
        self.btn_plot.setEnabled(False)
        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setContentsMargins(0,0,0,0)
        widget = QWidget(self)
        layout.addWidget(self.btn_plot)
        widget.setLayout(layout)
        widget.setGeometry(QtCore.QRect(100, 100, 10, 50))
        self.setCentralWidget(widget)

    def window2(self):                                             # <===
        self.w = Window2()
        self.w.plotTrajectory(filePath)
        self.w.show()
    

    def sendFilePath(self, fp):
        global filePath
        filePath = fp
        #self.plotTrajectory(fp)

    