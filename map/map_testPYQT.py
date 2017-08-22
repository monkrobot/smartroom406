from ESP32 import device

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit,
                             QLineEdit, QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPainter, QColor, QPen, QImage, QBrush)
from PyQt5.QtCore import (QCoreApplication, Qt, QPoint)

class Map(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()



    elHght, elWdth = 0, 0 #Mouse click WiFi zone
    elCntH, elCntW = 0, 0 #Mouse click WiFi zone center
    clickNum = 0 #Number of mouse click for device
    devList = [] #Device list
    elClr = "#000000"

    def mousePressEvent(self, event):

        painter = QPainter(self._im)
        painter.setPen(QPen(QColor(Map.elClr), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor(Map.elClr), Qt.CrossPattern))

        point = event.pos()
        painter.drawEllipse(point, Map.elHght, Map.elWdth)
        painter.drawEllipse(point, Map.elCntH, Map.elCntW)

        if Map.elHght >= 200:
            print("ClickNum:", Map.clickNum)

            #Mouse click coordinates
            pointPressX = point.x()
            pointPressY = point.y()
            print("X is", pointPressX)
            print("Y is", pointPressY)

            #New device
            dev = device.Device([pointPressX, pointPressY], Map.elHght)

            #Device list
            Map.devList.append(dev)
            print("Map.devList", Map.devList)

            Map.clickNum += 1
            #if Map.clickNum >= 1:
            #    device.calcWifiDist(Map.devList)



        # Перерисуемся
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        painter.drawImage(0, 0, self._im)

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        #Button Router
        btnRout = QPushButton("Router", self)
        btnRout.move(30, 50)

        btnESP = QPushButton("ESP-32", self)
        btnESP.move(160, 50)

        btnStp = QPushButton("Stop", self)
        btnStp.move(290, 50)


        btnShwInts = QPushButton("Result", self)
        #btnShwInts = btnStp = QPushButton("Result", self) #when click button, 2 buttons work (stop and Result)
        btnShwInts.move(420, 50)

        btnRout.clicked.connect(self.btnRoutnClicked)
        btnESP.clicked.connect(self.btnESPClicked)
        btnStp.clicked.connect(self.btnStopClicked)
        btnShwInts.clicked.connect(self.btnShwIntsClicked)

        #Size and color for drawing zone
        self._im = QImage(1700, 960, QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

        #Painting of room - rectangle
        painterRect = QPainter(self._im)
        painterRect.setPen(QPen(QColor("#000"), 1, Qt.SolidLine, Qt.RoundCap))
        painterRect.drawRect(100, 100, 1000, 800)

        #Size and Title for program window
        self.setFixedSize(1700, 960)
        self.setWindowTitle('Room')

        self.show()

    def btnRoutnClicked(self):
        '''
        Function for button Router
        Changes size and color of router's wifi zone
        '''
        Map.elHght, Map.elWdth = 300, 300
        Map.elCntH, Map.elCntW = 20, 20
        Map.elClr = "#431292"
        print("Button Router pressed")

    def btnESPClicked(self):
        '''
        Function for button ESP-32
        Changes size and color of esp's wifi zone
        '''
        Map.elHght, Map.elWdth = 200, 200
        Map.elCntH, Map.elCntW = 10, 10
        Map.elClr = "#439232"
        print("Button ESP-32 pressed")

    def btnStopClicked(self):
        '''
        Function for button Stop
        Changes size of wifi zone to 0
        '''
        Map.elHght, Map.elWdth = 0, 0
        Map.elCntH, Map.elCntW = 0, 0
        print("Button Stop pressed")
        print("Fuck you!")

    def btnShwIntsClicked(self):
        print("Button Show intersections pressed")
        if Map.clickNum >= 1:
            device.calcWifiDist(Map.devList)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    map = Map()
    sys.exit(app.exec_())