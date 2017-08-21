import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QWidget, QToolTip, QPushButton, QApplication, QTextEdit,
                             QLineEdit, QGridLayout, QMessageBox, QLabel, QFrame, QColorDialog, QFileDialog)
from PyQt5.QtGui import (QIcon, QFont, QPainter, QColor, QPen, QImage, QBrush)
from PyQt5.QtCore import (QCoreApplication, Qt, QPoint)

class Map(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()



    elHght, elWdth = 0, 0
    elCntH, elCntW = 0, 0
    elClr = "#000000"
    print("elClr", elClr)
    def mousePressEvent(self, event):

        painter = QPainter(self._im)
        painter.setPen(QPen(QColor(Map.elClr), 1, Qt.SolidLine, Qt.RoundCap))
        painter.setBrush(QBrush(QColor(Map.elClr), Qt.CrossPattern))

        point = event.pos()
        painter.drawEllipse(point, Map.elHght, Map.elWdth)
        painter.drawEllipse(point, Map.elCntH, Map.elCntW)

        #совместить с device.py
        pointPressX = point.x()
        pointPressY = point.y()
        print("Event position is:", point)
        print("X is", pointPressX)
        print("Y is", pointPressY)

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

        btnRout.clicked.connect(self.btnRoutnClicked)
        btnESP.clicked.connect(self.btnESPClicked)
        btnStp.clicked.connect(self.btnStopClicked)

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
        Map.elClr = "#431292" #"#684519"
        print("elClr", Map.elClr)
        print("Button Router pressed")

    def btnESPClicked(self):
        '''
        Function for button ESP-32
        Changes size and color of esp's wifi zone
        '''
        Map.elHght, Map.elWdth = 200, 200
        Map.elCntH, Map.elCntW = 10, 10
        Map.elClr = "#439232"
        print("elClr", Map.elClr)
        print("Button ESP-32 pressed")

    def btnStopClicked(self):
        '''
        Function for button Stop
        Changes size of wifi zone to 0
        '''
        Map.elHght, Map.elWdth = 0, 0
        Map.elCntH, Map.elCntW = 0, 0
        print("elClr", Map.elClr)
        print("Button Stop pressed")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    map = Map()
    sys.exit(app.exec_())