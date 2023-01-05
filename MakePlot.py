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
        exporter.export(plotPath + "/" + 'trajectory.png')






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
        X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5, X6, Y6, X7, Y7, X8, Y8, X9, Y9, X10, Y10, X11, Y11, X12, Y12, X13, Y13, X14, Y14, X15, Y15, X16, Y16, X17, Y17, X18, Y18, X19, Y19, X20, Y20, X21, Y21, X22, Y22, X23, Y23, X24, Y24, X25, Y25, X26, Y26, X27, Y27, X28, Y28, X29, Y29, X30, Y30, X31, Y31, X32, Y32, X33, Y33, X34, Y34, X35, Y35, X36, Y36, X37, Y37, X38, Y38, X39, Y39, X40, Y40, X41, Y41, X42, Y42, X43, Y43, X44, Y44, X45, Y45, X46, Y46, X47, Y47, X48, Y48, X49, Y49,  X50, Y50 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        

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

            if tid == 6:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X6.append(x2)
                Y6.append(y2)

            if tid == 7:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X7.append(x2)
                Y7.append(y2)

            
            if tid == 8:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X8.append(x2)
                Y8.append(y2)


            if tid == 9:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X9.append(x2)
                Y9.append(y2)


            if tid == 10:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X10.append(x2)
                Y10.append(y2)
            
            if tid == 11:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X11.append(x2)
                Y11.append(y2)
        

            if tid == 12:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X12.append(x2)
                Y12.append(y2)

            if tid == 13:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X13.append(x2)
                Y13.append(y2)

            if tid == 14:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X14.append(x2)
                Y14.append(y2)

            if tid == 15:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X15.append(x2)
                Y15.append(y2)


            if tid == 16:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X16.append(x2)
                Y16.append(y2)


            if tid == 17:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X17.append(x2)
                Y17.append(y2)


            if tid == 18:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X18.append(x2)
                Y18.append(y2)


            if tid == 19:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X19.append(x2)
                Y19.append(y2)


            if tid == 20:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X20.append(x2)
                Y20.append(y2)

            if tid == 21:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X21.append(x2)
                Y21.append(y2)

            if tid == 22:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X22.append(x2)
                Y22.append(y2)

            if tid == 23:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X23.append(x2)
                Y23.append(y2)


            if tid == 24:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X24.append(x2)
                Y24.append(y2)



            if tid == 25:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X25.append(x2)
                Y25.append(y2)


            if tid == 26:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X26.append(x2)
                Y26.append(y2)


            if tid == 27:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X27.append(x2)
                Y27.append(y2)


            if tid == 28:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X28.append(x2)
                Y28.append(y2)

            if tid == 29:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X29.append(x2)
                Y29.append(y2)

            if tid == 30:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X30.append(x2)
                Y30.append(y2)

            if tid == 31:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X31.append(x2)
                Y31.append(y2)

            if tid == 32:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X32.append(x2)
                Y32.append(y2)

            if tid == 33:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X33.append(x2)
                Y33.append(y2)

            if tid == 34:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X34.append(x2)
                Y34.append(y2)


            if tid == 35:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X35.append(x2)
                Y35.append(y2)


            if tid == 36:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X36.append(x2)
                Y36.append(y2)


            if tid == 37:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X37.append(x2)
                Y37.append(y2)


            if tid == 38:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X38.append(x2)
                Y38.append(y2)


            if tid == 39:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X39.append(x2)
                Y39.append(y2)


            if tid == 40:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X40.append(x2)
                Y40.append(y2)

            if tid == 41:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X41.append(x2)
                Y41.append(y2)


            if tid == 42:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X42.append(x2)
                Y42.append(y2)


            if tid == 43:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X43.append(x2)
                Y43.append(y2)


            if tid == 44:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X44.append(x2)
                Y44.append(y2)


            if tid == 45:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X45.append(x2)
                Y45.append(y2)


            if tid == 46:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X46.append(x2)
                Y46.append(y2)


            if tid == 47:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X47.append(x2)
                Y47.append(y2)


            if tid == 48:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X48.append(x2)
                Y48.append(y2)


            if tid == 49:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X49.append(x2)
                Y49.append(y2)


            if tid == 50:
                x2 = float(''.join(filter(str.isdigit, x)))
                y2 = float(''.join(filter(str.isdigit, y)))
                x2 = x2/1000
                y2 = y2/1000
                X50.append(x2)
                Y50.append(y2)

        self.plot(X1, Y1, "Tracker ID: 1", 'y')
        self.plot(X2, Y2, "Tracker ID: 2", 'm')
        self.plot(X3, Y3, "Tracker ID: 3", 'w')
        self.plot(X4, Y4, "Tracker ID: 4", 'l')
        self.plot(X5, Y5, "Tracker ID: 5", 'b')
        self.plot(X6, Y6, "Tracker ID: 6", 'g')
        self.plot(X7, Y7, "Tracker ID: 7", 'r')
        self.plot(X8, Y8, "Tracker ID: 8", 'b')
        self.plot(X9, Y9, "Tracker ID: 9", 'g')
        self.plot(X10, Y10, "Tracker ID: 10", 'l')
        self.plot(X11, Y11, "Tracker ID: 11", 'd')
        self.plot(X12, Y12, "Tracker ID: 12", 'c')
        self.plot(X13, Y13, "Tracker ID: 13", 'r')
        self.plot(X14, Y14, "Tracker ID: 14", 'm')
        self.plot(X15, Y15, "Tracker ID: 15", 'w')
        self.plot(X16, Y16, "Tracker ID: 16", 'y')
        self.plot(X17, Y17, "Tracker ID: 17", 'r')
        self.plot(X18, Y18, "Tracker ID: 18", 'g')
        self.plot(X19, Y19, "Tracker ID: 19", 'w')
        self.plot(X20, Y20, "Tracker ID: 20", 'b')
        self.plot(X21, Y21, "Tracker ID: 21", 'r')
        self.plot(X22, Y22, "Tracker ID: 22", 'r')
        self.plot(X23, Y23, "Tracker ID: 23", 'r')
        self.plot(X24, Y24, "Tracker ID: 24", 'r')
        self.plot(X25, Y25, "Tracker ID: 25", 'r')
        self.plot(X26, Y26, "Tracker ID: 26", 'r')
        self.plot(X27, Y27, "Tracker ID: 27", 'r')
        self.plot(X28, Y28, "Tracker ID: 28", 'r')
        self.plot(X29, Y29, "Tracker ID: 29", 'r')
        self.plot(X30, Y30, "Tracker ID: 30", 'r')
        self.plot(X31, Y31, "Tracker ID: 31", 'r')
        self.plot(X32, Y32, "Tracker ID: 32", 'r')
        self.plot(X33, Y33, "Tracker ID: 33", 'r')
        self.plot(X34, Y34, "Tracker ID: 34", 'r')
        self.plot(X35, Y35, "Tracker ID: 35", 'r')
        self.plot(X36, Y36, "Tracker ID: 36", 'r')
        self.plot(X37, Y37, "Tracker ID: 37", 'r')
        self.plot(X38, Y38, "Tracker ID: 38", 'r')
        self.plot(X39, Y39, "Tracker ID: 39", 'r')
        self.plot(X40, Y40, "Tracker ID: 40", 'r')
        self.plot(X41, Y41, "Tracker ID: 41", 'r')
        self.plot(X42, Y42, "Tracker ID: 42", 'r')
        self.plot(X43, Y43, "Tracker ID: 43", 'r')
        self.plot(X44, Y44, "Tracker ID: 44", 'r')
        self.plot(X45, Y45, "Tracker ID: 45", 'r')
        self.plot(X46, Y46, "Tracker ID: 46", 'r')
        self.plot(X47, Y47, "Tracker ID: 47", 'r')
        self.plot(X48, Y48, "Tracker ID: 48", 'r')
        self.plot(X49, Y49, "Tracker ID: 49", 'r')
        self.plot(X50, Y50, "Tracker ID: 50", 'r')
        

        
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
    

    def sendFilePath(self, fp, pp):
        global filePath, plotPath
        filePath = fp
        plotPath = pp
        #self.plotTrajectory(fp)

    