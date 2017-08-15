import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Room:
    def __init__(self, long, width, points=[0,0]):
        self.long = long
        self.width = width
        #self.height = height
        self.points = points

    def drawingRoom(self):
        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111, aspect='equal')
        ax2.add_patch(
            patches.Rectangle(
                (0.1, 0.1),
                self.width,
                self.long,
                fill=False  # remove background
            )
        )
        ax2.add_patch(
            patches.Circle(
                (self.points),
                radius=0.3,
                edgecolor="red",
                fill=False
            )
        )
        ax2.add_patch(
            patches.Circle(
                (self.points),
                radius=0.01,
                edgecolor="red",
                fill=False
            )
        )

        plt.show()


testRoom = Room(0.8, 0.5, points=[0.2, 0.4])
testRoom.drawingRoom()

