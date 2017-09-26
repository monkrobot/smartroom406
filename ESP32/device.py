import math

#radius of wifi signal
type= {"router": [0.5], "esp": [0.1]}



class Device:
    '''Class for devices: router and esp-32'''
    def __init__(self, position=[0,0], radius=0.1):
        self.position = position
        self.radius = radius
        self.id
        self.links = []
    def addLink(id, speed):

    def deleteLink(id):

#Devices
#wifirad =
dev = Device([0,0],3)
dev2 = Device([1,3],2)
dev3 = Device([1,1], 4)

devices = [dev,dev2,dev3]

print('devices', devices)


#function for calculation radius and distance between two wifi points
def calcWifiDist(devices):
    for i in range(len(devices)):
        intersecList = []
        #intersecDic = {}
        for j in range(len(devices)):
            if j == i:
                continue
            else:
                #if math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                #    devices[j].position[1] - devices[i].position[1]) ** 2) > devices[i].radius[-1]:
                #    #print("No signal. It's too far")
                #    continue
                #else:
                if math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[0]:
                    intersecList.append([j+1, 72])
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[1]:
                    intersecList.append([j+1, 54])
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[2]:
                    intersecList.append([j + 1, 32])
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                    devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[3]:
                    intersecList.append([j + 1, 11])
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                    devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[4]:
                    intersecList.append([j + 1, 6])
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                    devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[5]:
                    intersecList.append([j + 1, 1])
                else:
                    continue


                    #intersecDic[str(j+1)] = 'speed'
                    #print("Good")
        print(i+1, ":", intersecList)
        #print(i + 1, ":", intersecDic)



        #if math.sqrt((devices[i+1].position[0]-devices[i].position[0])**2 +
        #                             (devices[i + 1].position[1] - devices[i].position[1]) ** 2) > devices[i].radius:
        #    print("No signal. It's too far")
        #else:
        #    print("Good")


if __name__ == "__main__":
    calcWifiDist(devices)