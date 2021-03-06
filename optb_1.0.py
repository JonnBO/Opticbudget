#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_calc(object):
    def setupUi(self, calc):
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget = QtWidgets.QWidget(calc)
        calc.setWindowTitle(_translate("calc", "Расчет оптического Бюджета"))
        calc.resize(890, 280) 
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Start = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(10, 10, 60, 31))
        self.Start.setMinimum(-30.0)
        self.Start.setMaximum(30.0)
        self.Start.setSingleStep(0.1)
        self.lineStart = QtWidgets.QFrame(self.centralwidget)
        self.lineStart.setGeometry(QtCore.QRect(30, 40, 20, 70))
        self.lineStart.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.lineStart.setFrameShape(QtWidgets.QFrame.VLine)
        self.frames = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "m7", "m9", "m10"]
        self.frames_coords = [10, 100, 190, 280, 370, 460, 550, 640, 730, 820, 820] #Координаты по х
        self.frames_ends =["m1e", "m2e", "m3e", "m4e", "m5e", "m6e", "m7e", "m7e", "m9e", "m101e", "m102e"]
        self.splitters_count = ["5/95", "10/90", "15/85", "20/80", "25/75", "30/70", "35/65", "40/60", "45/55", "50/50", "55/45", "60/40", "65/35", "70/30", "75/25", "80/20", "85/15", "90/10", "95/5", "100/0", "0/100"]
        self.splitters_count_ends = ["1/2", "1/4", "1/8", "1/16"]
        self.labels_signal_road = ["lsr"] * 10
        self.labels_signal_end = ["lse"] * 10
        self.labels_signal_abonent = ["lsa"] * 11
        self.splitters = ["spl"] * 10
        self.splitters_abonents = ["spla"] * 11
        self.lines_magistral = ["lm"] * 9
        self.lines_abonent = ["la"] * 10
        self.line_coords = [30, 120, 210, 300, 390, 480, 570, 660, 750, 840, 840]
        self.frames_ends[10] = QtWidgets.QFrame(self.centralwidget) #Create frames ends
        self.frames_ends[10].setGeometry(QtCore.QRect(self.frames_coords[10], 10, 60, 60)) #Set coordinates frames
        self.splitters_abonents[10] = QtWidgets.QComboBox(self.frames_ends[10]) #Create box splitters abonent
        self.splitters_abonents[10].setGeometry(QtCore.QRect(0, 0, 60, 20)) #Set coordinates box splitters abonent
        self.labels_signal_abonent[10] = QtWidgets.QLabel(self.frames_ends[10]) #Create abonent labels
        self.labels_signal_abonent[10].setGeometry(QtCore.QRect(0, 20, 60, 20)) #Set coordinates abonent labels
        self.labels_signal_abonent[10].setStyleSheet("background-color: rgb(127, 127, 127);") #Set style abonent labels
        self.lines_abonent[9] = QtWidgets.QFrame(self.centralwidget)
        self.lines_abonent[9].setGeometry(QtCore.QRect(self.line_coords[9], 50, 20, 60))
        self.lines_abonent[9].setStyleSheet("background-color: rgb(100, 200, 255);")
        self.lines_abonent[9].setFrameShape(QtWidgets.QFrame.VLine)
        for fr in range (0, len(self.frames)):
            self.frames[fr] = QtWidgets.QFrame(self.centralwidget) #Create frames
            self.frames[fr].setGeometry(QtCore.QRect(self.frames_coords[fr], 110, 60, 60)) #Set coordinates frames 
            self.labels_signal_road[fr] = QtWidgets.QLabel(self.frames[fr]) #Create magistral labels
            self.labels_signal_road[fr].setGeometry(QtCore.QRect(0, 20, 60, 20)) #Set coordinates of magistral labels
            self.labels_signal_road[fr].setStyleSheet("background-color: rgb(170, 127, 127);") #Set style of magistral labels
            self.labels_signal_road[fr].setAlignment(QtCore.Qt.AlignCenter)#Set alignment of magistral labels
            self.labels_signal_end[fr] = QtWidgets.QLabel(self.frames[fr]) #Create magistral labels
            self.labels_signal_end[fr].setGeometry(QtCore.QRect(0, 40, 60, 20)) #Set coordinates of magistral labels
            self.labels_signal_end[fr].setStyleSheet("background-color: rgb(85, 170, 255);") #Set style of magistral labels
            self.labels_signal_end[fr].setAlignment(QtCore.Qt.AlignCenter)#Set alignment of magistral labels            
            self.splitters[fr] = QtWidgets.QComboBox(self.frames[fr]) #Create box of splitters
            self.splitters[fr].setGeometry(QtCore.QRect(0, 0, 60, 20))#Set coordinates of box splitters
            self.frames_ends[fr] = QtWidgets.QFrame(self.centralwidget) #Create frames ends
            self.frames_ends[fr].setGeometry(QtCore.QRect(self.frames_coords[fr], 230, 60, 60)) #Set coordinates frames
            self.splitters_abonents[fr] = QtWidgets.QComboBox(self.frames_ends[fr]) #Create box splitters abonent
            self.splitters_abonents[fr].setGeometry(QtCore.QRect(0, 0, 60, 20)) #Set coordinates box splitters abonent
            self.labels_signal_abonent[fr] = QtWidgets.QLabel(self.frames_ends[fr]) #Create abonent labels
            self.labels_signal_abonent[fr].setGeometry(QtCore.QRect(0, 20, 60, 20)) #Set coordinates abonent labels
            self.labels_signal_abonent[fr].setStyleSheet("background-color: rgb(127, 127, 127);") #Set style abonent labels
        for l in range (0, len(self.lines_magistral)):
            self.lines_magistral[l] = QtWidgets.QFrame(self.centralwidget)
            self.lines_magistral[l].setGeometry(QtCore.QRect(self.line_coords[l] + 40, 130, 30, 20))
            self.lines_magistral[l].setStyleSheet("background-color: rgb(255, 150, 150);")
            self.lines_magistral[l].setFrameShape(QtWidgets.QFrame.HLine)
        for l in range(0, len(self.lines_abonent)):
            self.lines_abonent[l] = QtWidgets.QFrame(self.centralwidget)
            self.lines_abonent[l].setGeometry(QtCore.QRect(self.line_coords[l], 170, 20, 60))
            self.lines_abonent[l].setStyleSheet("background-color: rgb(100, 200, 255);")
            self.lines_abonent[l].setFrameShape(QtWidgets.QFrame.VLine)
        for s in range(0,len(self.splitters)):
            for l in range(0,21):
                self.splitters[s].addItem("")
                self.splitters[s].setItemText(l, _translate("calc", self.splitters_count[l]))#Set text items in box splitters
            self.splitters[s].setFont(font)
        for s in range(0,len(self.splitters_abonents)):
            for l in range(0,4):
                self.splitters_abonents[s].addItem("")
                self.splitters_abonents[s].setItemText(l, _translate("calc", self.splitters_count_ends[l]))#Set text items in box splitters
                self.splitters_abonents[s].setFont(font)
        self.Losts_n_m = [0.32, 0.49, 0.76, 1.06, 1.42, 1.56, 1.93, 2.34, 2.71, 3.19, 3.73, 4.01, 4.56, 5.39, 6.29, 7.11, 8.16, 10.08, 13.7, 100, 0] # затухания на магистрали
        self.losts_n_a = [13.7, 10.08, 8.16, 7.11, 6.29, 5.39, 4.56, 4.01, 3.73, 3.17, 2.71, 2.34, 1.93, 1.56, 1.42, 1.06, 0.76, 0.49, 0.32, 0, 100] # затухания на абонентах
        self.losts_r = [4.3, 7.4, 10.7, 13.9] #Затухание равномерников
        calc.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(calc)    
        self.Start.valueChanged.connect(lambda:self.calculate(self.labels_signal_road, self.labels_signal_end, self.labels_signal_abonent, self.Losts_n_m, self.losts_n_a, self.losts_r, self.splitters, self.splitters_abonents, self.Start))
        for index in (self.splitters + self.splitters_abonents):
            index.currentIndexChanged.connect(lambda:self.calculate(self.labels_signal_road, self.labels_signal_end, self.labels_signal_abonent, self.Losts_n_m, self.losts_n_a, self.losts_r, self.splitters, self.splitters_abonents, self.Start))
    def calculate(self, labels_signal_road, labels_signal_end, labels_signal_abonent, Losts_n_m, losts_n_a, losts_r, splitters, splitters_abonents, start):
        self.labels_signal_road[0].setText(str(round((start.value() - Losts_n_m[splitters[0].currentIndex()]),2)))
        self.labels_signal_end[0].setText(str(round((start.value() - losts_n_a[splitters[0].currentIndex()]),2)))
        for road in range (1, len(labels_signal_road)):
            labels_signal_road[road].setText(str(round((float(labels_signal_road[road - 1].text()) - Losts_n_m[splitters[road].currentIndex()]),2)))
            labels_signal_end[road].setText(str(round((float(labels_signal_road[road - 1].text()) - losts_n_a[splitters[road].currentIndex()]),2)))
        for abonents in range (0, len(labels_signal_abonent)):
            if abonents == 10: 
                labels_signal_abonent[10].setText(str(round((float(labels_signal_end[9].text()) - losts_r[splitters_abonents[10].currentIndex()]), 2)))    
            else:
                labels_signal_abonent[abonents].setText(str(round((float(labels_signal_end[abonents].text()) - losts_r[splitters_abonents[abonents].currentIndex()]), 2)))
        for color in labels_signal_abonent: #цветовая индикация сигнала
            color.setStyleSheet("background-color: rgb(60, 179, 113);")
            if float(color.text()) < -27:
                color.setStyleSheet("background-color: rgb(205, 92, 92);")
            elif float(color.text()) < -23:
                color.setStyleSheet("background-color: rgb(255, 255, 0);")  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calc = QtWidgets.QMainWindow()
    ui = Ui_calc()
    ui.setupUi(calc)
    calc.show()
    sys.exit(app.exec_())
