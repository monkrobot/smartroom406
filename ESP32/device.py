import math

#radius of wifi signal
type= {"router": [0.5], "esp": [0.1]}



class Device:
    '''Class for devices: router and esp-32'''
    def __init__(self, id, position=[0,0], radius=0.1):
        self.position = position
        self.radius = radius
        self.id = id
        self.links = []
    def addLink(self, id, speed):
        self.links.append({id: speed})
    def deleteLink(self, id_del):
        for i in self.links:
            if id_del in i:
                self.links.remove(i)
                break
            else:
                continue

#Devices
#wifirad =
#radiusWiFi = [Map.elHght_72, Map.elHght_54, Map.elHght_32, Map.elHght_11, Map.elHght_6, Map.elHght_1]
radiusWiFi = [1,6,11,32,54,72]
dev = Device(1,[0,0],radiusWiFi)
dev2 = Device(2,[2,3],radiusWiFi)
dev3 = Device(3,[20,1], radiusWiFi)
dev4 = Device(3,[0,134], radiusWiFi)
dev5 = Device(3,[12,1], radiusWiFi)
dev6 = Device(3,[67,1], radiusWiFi)
dev7 = Device(3,[0,54], radiusWiFi)

devices = [dev,dev2,dev3,dev4,dev5,dev6,dev7]


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
                    intersecList.append({j + 1: 72})
                    devices[i].addLink(j+1,72)
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[1]:
                    intersecList.append({j + 1: 54})
                    devices[i].addLink(j + 1, 54)
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[2]:
                    intersecList.append({j + 1: 32})
                    devices[i].addLink(j + 1, 32)
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[3]:
                    intersecList.append({j + 1: 11})
                    devices[i].addLink(j + 1, 11)
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[4]:
                    intersecList.append({j + 1: 6})
                    devices[i].addLink(j + 1, 6)
                elif math.sqrt((devices[j].position[0] - devices[i].position[0]) ** 2 + (
                            devices[j].position[1] - devices[i].position[1]) ** 2) < devices[i].radius[5]:
                    intersecList.append({j + 1: 1})
                    devices[i].addLink(j + 1, 1)
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
    print("connections:")
    calcWifiDist(devices)
    print(' ')
    for i in range(len(devices)):
        print("devLink for", i+1, devices[i].links)
        devices[i].deleteLink(2)
        print("devLink after delete for", i + 1, devices[i].links)
        print(' ')