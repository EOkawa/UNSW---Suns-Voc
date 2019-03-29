# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Suns-Voc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import PyQt5
import sys
import random

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Main window parameters
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 320)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 600))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Push buttons
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.addBtn.setObjectName("addBtn")
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitBtn.setGeometry(QtCore.QRect(640, 250, 71, 21))
        self.quitBtn.setObjectName("quitBtn")
        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.removeBtn.setObjectName("removeBtn")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(570, 250, 71, 21))
        self.startBtn.setObjectName("startBtn")
        self.loadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn.setGeometry(QtCore.QRect(20, 220, 71, 21))
        self.loadBtn.setObjectName("loadBtn")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(640, 30, 71, 21))
        self.saveBtn.setObjectName("saveBtn")

        # Lists
        self.temperatureList = QtWidgets.QListWidget(self.centralwidget)
        self.temperatureList.setGeometry(QtCore.QRect(100, 80, 111, 161))
        self.temperatureList.setObjectName("temperatureList")

        # Numeric controls
        self.AverageNum = QtWidgets.QSpinBox(self.centralwidget)
        self.AverageNum.setGeometry(QtCore.QRect(510, 250, 42, 22))
        self.AverageNum.setObjectName("AverageNum")

        # Decorations
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 20, 20, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(20, 80, 71, 22))
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        # Lists
        self.vocList = QtWidgets.QListWidget(self.centralwidget)
        self.vocList.setGeometry(QtCore.QRect(220, 80, 111, 161))
        self.vocList.setObjectName("vocList")

        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 240, 191, 31))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 230, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 60, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 51, 16))
        self.label_4.setObjectName("label_4")


        m = PlotCanvas(MainWindow, width=5, height=4)
        m.move(390,60)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addBtn.clicked.connect(self.addTemperature)
        self.quitBtn.clicked.connect(self.quitProgram)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "Add"))
        self.quitBtn.setText(_translate("MainWindow", "QUIT"))
        self.removeBtn.setText(_translate("MainWindow", "Remove"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.loadBtn.setText(_translate("MainWindow", "Load from file"))
        self.label.setText(_translate("MainWindow", "Select desired temperatures for measurement"))
        self.label_2.setText(_translate("MainWindow", "Averages"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Temperature"))
        self.label_4.setText(_translate("MainWindow", "Voc"))

    def addTemperature(self):
        value = self.doubleSpinBox.text()
        self.doubleSpinBox.clear()
        self.temperatureList.addItem(value)

    def quitProgram(self):
        quit()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
