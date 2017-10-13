from ESP32 import device

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit,
                             QLineEdit, QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPainter, QColor, QPen, QImage, QBrush)
from PyQt5.QtCore import (QCoreApplication, Qt, QPoint)

#ESP Bluetooth radius for diff speeds
bltWidth_72 = [0, 0]
bltWidth_54 = [0, 0]
bltWidth_32 = [0, 0]
bltWidth_11 = [0, 0]
bltWidth_3 = [9, 9]
bltWidth_2 = [46, 46]
bltWidth_Cnt = [1, 1]

#Router Wi-Fi radius for diff speeds
rtrWidth = [300, 300]
rtrCnt = [20, 20]

width_stop = [0, 0]

#Bluetooth speed
bluetooth_speed = [72,54,32,11,3,2]


class Map(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()



    elHght_72, elWdth_72 = 0, 0 #Mouse click WiFi zone
    elHght_54, elWdth_54 = 0, 0
    elHght_32, elWdth_32 = 0, 0
    elHght_11, elWdth_11 = 0, 0
    elHght_3, elWdth_3 = 0, 0
    elHght_2, elWdth_2 = 0, 0
    elCntH, elCntW = 0, 0 #Mouse click WiFi zone center

    clickNum = 0 #Number of mouse click for device

    devList = [] #Device list

    elClr = "#000000"

    def mousePressEvent(self, event):

        point = event.pos()

        painter = QPainter(self._im)
        painter.setPen(QPen(QColor(Map.elClr), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor(Map.elClr), Qt.SolidPattern))
        painter.drawEllipse(point, Map.elCntH, Map.elCntW)

        painter.setPen(QPen(QColor("#000"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#000"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_72, Map.elWdth_72)

        painter.setPen(QPen(QColor("#439232"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#439232"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_54, Map.elWdth_54)

        painter.setPen(QPen(QColor("#923243"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#923243"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_32, Map.elWdth_32)

        painter.setPen(QPen(QColor("#324392"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#324392"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_11, Map.elWdth_11)

        painter.setPen(QPen(QColor("#324392"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#324392"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_3, Map.elWdth_3)

        painter.setPen(QPen(QColor("#324392"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#324392"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_2, Map.elWdth_2)

        if Map.elHght_2 >= 10:

            painter.setPen(QPen(QColor("#000000")))
            painter.setFont(QFont('Arial', 15))
            painter.drawText(point, str(Map.clickNum + 1))

            print("ClickNum:", Map.clickNum + 1)

            #Mouse click coordinates
            pointPressX = point.x()
            pointPressY = point.y()
            print("X is", pointPressX)
            print("Y is", pointPressY)

            #New device
            radiusBlt = [Map.elHght_72, Map.elHght_54, Map.elHght_32, Map.elHght_11, Map.elHght_3, Map.elHght_2]
            dev = device.Device(Map.clickNum + 1, [pointPressX, pointPressY], radiusBlt)

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

        btnBlt = QPushButton("Bluetooth", self)
        btnBlt.move(160, 50)

        btnStp = QPushButton("Stop", self)
        btnStp.move(290, 50)


        btnShwInts = QPushButton("Result", self)
        #btnShwInts = btnStp = QPushButton("Result", self) #when click button, 2 buttons work (stop and Result)
        btnShwInts.move(420, 50)

        btnRout.clicked.connect(self.btnRoutnClicked)
        btnBlt.clicked.connect(self.btnBltClicked)
        btnStp.clicked.connect(self.btnStopClicked)
        btnShwInts.clicked.connect(self.btnShwIntsClicked)

        #Size and color for drawing zone
        self._im = QImage(1700, 960, QImage.Format_ARGB32)
        self._im.fill(QColor("white"))

        #Painting of room - rectangle
        painterRect = QPainter(self._im)
        painterRect.setPen(QPen(QColor("#000"), 1, Qt.SolidLine, Qt.RoundCap))
        painterRect.drawRect(100, 100, 100, 800)

        #Size and Title for program window
        self.setFixedSize(1700, 960)
        self.setWindowTitle('Room')

        self.show()

    def btnRoutnClicked(self):
        '''
        Function for button Router
        Changes size and color of router's wifi zone
        '''
        Map.elHght_72, Map.elWdth_72 = rtrWidth
        #Map.elHght_54, Map.elWdth_54
        #Map.elHght_32, Map.elWdth_32
        #Map.elHght_11, Map.elWdth_11
        #Map.elHght_6, Map.elWdth_6
        #Map.elHght_1, Map.elWdth_1
        Map.elCntH, Map.elCntW = rtrCnt
        Map.elClr = "#431292"
        print("Button Router pressed")

    def btnBltClicked(self):
        '''
        Function for button Bluetooth
        Changes size and color of esp's bluetooth zone
        '''
        Map.elHght_72, Map.elWdth_72 = bltWidth_72
        Map.elHght_54, Map.elWdth_54 = bltWidth_54
        Map.elHght_32, Map.elWdth_32 = bltWidth_32
        Map.elHght_11, Map.elWdth_11 = bltWidth_11
        Map.elHght_3, Map.elWdth_3 = bltWidth_3
        Map.elHght_2, Map.elWdth_2 = bltWidth_2
        Map.elCntH, Map.elCntW = bltWidth_Cnt
        Map.elClr = "#439232"
        print("Button Bluetooth pressed")

    def btnStopClicked(self):
        '''
        Function for button Stop
        Changes size of bluetooth zone to 0
        '''
        Map.elHght_72, Map.elWdth_72 = width_stop
        Map.elHght_54, Map.elWdth_54 = width_stop
        Map.elHght_32, Map.elWdth_32 = width_stop
        Map.elHght_11, Map.elWdth_11 = width_stop
        Map.elHght_3, Map.elWdth_3 = width_stop
        Map.elHght_2, Map.elWdth_2 = width_stop
        Map.elCntH, Map.elCntW = width_stop
        print("Button Stop pressed")

    def btnShwIntsClicked(self):
        print("Button Show intersections pressed")
        if Map.clickNum >= 1:
            speed = bluetooth_speed
            device.calcWifiDist(Map.devList, bluetooth_speed)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    map = Map()
    sys.exit(app.exec_())