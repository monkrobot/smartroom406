import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Room:
    def __init__(self, long, width, points=([0,0]), wifiNum=1):
        self.long = long
        self.width = width
        #self.height = height
        self.points = points
        self.wifiNum = wifiNum

        self.fig2 = plt.figure()
        self.ax2 = self.fig2.add_subplot(111, aspect='equal')

    def drawingRoom(self):

        #Drawing rectangle-room
        self.ax2.add_patch(
            patches.Rectangle(
                (0.1, 0.1), #coordinates of left-bottom point
                self.width,
                self.long,
                fill=False  # remove background
            )
        )
        for i in range(self.wifiNum):
            self.drawingWifiZone(self.points[i])
            print(self.points[i])
        plt.show()

    #Drawing circle-wifi zone
    def drawingWifiZone(self, center):
       self.ax2.add_patch(
           patches.Circle(
               center,
               radius=0.3,
               edgecolor="red",
               fill=False
           )
       )
       #Drawing circle-point of wifi router
       self.ax2.add_patch(
           patches.Circle(
               center,
               radius=0.01,
               edgecolor="red",
               fill=False
           )
       )


testRoom = Room(0.8, 0.5, points=([0.2, 0.4],[0.3, 0.2],[0.1,0.1]), wifiNum=3)
testRoom.drawingRoom()

