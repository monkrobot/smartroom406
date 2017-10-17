from ESP32 import device

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit,
                             QLineEdit, QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPainter, QColor, QPen, QImage, QBrush)
from PyQt5.QtCore import (QCoreApplication, Qt, QPoint)

#ESP Wi-Fi radius for diff speeds
espWidth_72 = [22, 22]
espWidth_54 = [34, 34]
espWidth_32 = [58.5, 58.5]
espWidth_11 = [220, 220]
espWidth_6 = [277, 277]
espWidth_1 = [492, 492]
espWidth_Cnt = [5, 5]

#Router Wi-Fi radius for diff speeds
rtrWidth = [300, 300]
rtrCnt = [20, 20]

width_stop = [0, 0]

#Wi-Fi speed
wifi_speed = [72,54,32,11,6,1]


class Map(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()



    elHght_72, elWdth_72 = 0, 0 #Mouse click WiFi zone
    elHght_54, elWdth_54 = 0, 0
    elHght_32, elWdth_32 = 0, 0
    elHght_11, elWdth_11 = 0, 0
    elHght_6, elWdth_6 = 0, 0
    elHght_1, elWdth_1 = 0, 0
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
        painter.drawEllipse(point, Map.elHght_6, Map.elWdth_6)

        painter.setPen(QPen(QColor("#324392"), 2, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor("#324392"), Qt.CrossPattern))
        painter.drawEllipse(point, Map.elHght_1, Map.elWdth_1)

        if Map.elHght_1 >= 10:

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
            radiusWiFi = [Map.elHght_72, Map.elHght_54, Map.elHght_32, Map.elHght_11, Map.elHght_6, Map.elHght_1]
            dev = device.Device(Map.clickNum + 1, [pointPressX, pointPressY], radiusWiFi)

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
        painterRect.drawRect(100, 100, 100, 800)

        ##History
#
        ## Size and color for drawing zone
        #self._in = QImage(1700, 960, QImage.Format_ARGB32)
        #self._in.fill(QColor("red"))
        #
        ##Color for speed 72Mbps
        #history = QPainter(self._in)
        #history.setPen(QPen(QColor("#439232"), 1, Qt.SolidLine, Qt.RoundCap))
        ##history_72.setBrush(QBrush(QColor("#439232"), Qt.CrossPattern))
        #history.drawRect(400, 100, 100, 800)
#
        ## Color for speed 54Mbps
        #history_54 = QPainter(self._im)
        #history_54.setPen(QPen(QColor("#923243"), 1, Qt.SolidLine, Qt.RoundCap))
        #history_54.setBrush(QBrush(QColor("#923243"), Qt.CrossPattern))
        #history_54.drawRect(50, 150, 50, 50)
#
        ## Color for speed 32Mbps
        #history_32 = QPainter(self._im)
        #history_32.setPen(QPen(QColor("#324392"), 1, Qt.SolidLine, Qt.RoundCap))
        #history_32.setBrush(QBrush(QColor("#324392"), Qt.CrossPattern))
        #history_32.drawRect(50, 200, 50, 50)
#
        ## Color for speed 11Mbps
        #history_11 = QPainter(self._im)
        #history_11.setPen(QPen(QColor("#000"), 1, Qt.SolidLine, Qt.RoundCap))
        #history_11.setBrush(QBrush(QColor("#000"), Qt.CrossPattern))
        #history_11.drawRect(50, 250, 50, 50)
#
        ## Color for speed 6Mbps
        #history_6 = QPainter(self._im)
        #history_6.setPen(QPen(QColor("#000"), 1, Qt.SolidLine, Qt.RoundCap))
        #history_6.setBrush(QBrush(QColor("#000"), Qt.CrossPattern))
        #history_6.drawRect(50, 300, 50, 50)
#
        ## Color for speed 1Mbps
        #history_1 = QPainter(self._im)
        #history_1.setPen(QPen(QColor("#000"), 1, Qt.SolidLine, Qt.RoundCap))
        #history_1.setBrush(QBrush(QColor("#000"), Qt.CrossPattern))
        #history_1.drawRect(50, 350, 50, 50)

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

    def btnESPClicked(self):
        '''
        Function for button ESP-32
        Changes size and color of esp's wifi zone
        '''
        Map.elHght_72, Map.elWdth_72 = espWidth_72
        Map.elHght_54, Map.elWdth_54 = espWidth_54
        Map.elHght_32, Map.elWdth_32 = espWidth_32
        Map.elHght_11, Map.elWdth_11 = espWidth_11
        Map.elHght_6, Map.elWdth_6 = espWidth_6
        Map.elHght_1, Map.elWdth_1 = espWidth_1
        Map.elCntH, Map.elCntW = espWidth_Cnt
        Map.elClr = "#439232"
        print("Button ESP-32 pressed")

    def btnStopClicked(self):
        '''
        Function for button Stop
        Changes size of wifi zone to 0
        '''
        Map.elHght_72, Map.elWdth_72 = width_stop
        Map.elHght_54, Map.elWdth_54 = width_stop
        Map.elHght_32, Map.elWdth_32 = width_stop
        Map.elHght_11, Map.elWdth_11 = width_stop
        Map.elHght_6, Map.elWdth_6 = width_stop
        Map.elHght_1, Map.elWdth_1 = width_stop
        Map.elCntH, Map.elCntW = width_stop
        print("Button Stop pressed")

    def btnShwIntsClicked(self):
        print("Button Show intersections pressed")
        if Map.clickNum >= 1:
            speed = wifi_speed
            device.calcWifiDist(Map.devList, wifi_speed)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    map = Map()
    sys.exit(app.exec_())