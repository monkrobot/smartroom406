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


class Device(WifiStandard):
    def __init__(self, prot):
        self.prot = wifi_prots[prot]
        super().__init__(self.prot["maxSpeed"], wifi_prots[prot]["freq"], wifi_prots[prot]["signal"])


device = Device('prot802_11b')
print('Device wifi protocol: ', device.prot)
print("speed: ", device.maxSpeed)
