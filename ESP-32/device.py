import math

class Device:
    '''Class for devices: router and esp-32'''
    def __init__(self, position=[0,0], radius=0.1):
        self.position = position
        self.radius = radius

#Devices
dev = Device([0,0],3)
dev2 = Device([1,3],2)
dev3 = Device([1,1], 4)

devices = [dev,dev2,dev3]

#function for calculation radius and distance between two wifi points
def calcWifiDist():
    for i in range(len(devices)-1):
        if math.sqrt((devices[i+1].position[0]-devices[i].position[0])**2 +
                                     (devices[i + 1].position[1] - devices[i].position[1]) ** 2) > devices[i].radius:
            print("No signal. It's too far")
        else:
            print("Good")

calcWifiDist()