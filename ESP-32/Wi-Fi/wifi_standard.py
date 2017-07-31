'''Class for determining the wi-fi standard'''

import json
from pprint import pprint

with open('prot_wifi.json') as data_file:
    wifi_prots = json.load(data_file)

pprint(wifi_prots)
print('\n')

class WifiStandard:
    '''Parent-class for determing the wi-fi standard'''
    def __init__(self, maxSpeed, freq, signal):
        self.maxSpeed = maxSpeed
        self.freq = freq
        self.signal = signal


class Device():
    def __init__(self, prots):
        for prot in prots:
            #self.prot = wifi_prots[prot]
            setattr(self, prot, WifiStandard(wifi_prots[prot]["maxSpeed"], wifi_prots[prot]["freq"], wifi_prots[prot]["signal"]))



if __name__ == "__main__":
    device = Device(["prot802_11", "prot802_11a", "prot802_11b", "prot802_11g", "prot802_11n", "prot802_11ac"])

    print("speed: ", device.prot802_11.maxSpeed)
    print("freq: ", device.prot802_11.freq)
