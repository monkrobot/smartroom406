'''Class for determining the wi-fi standard and counting number of wi-fi devices use one of the standards'''


class WifiStandard:
    '''Parent-class for determing the wi-fi standard'''
    def __init__(self, maxSpeed, freq, signal):
        self.maxSpeed = maxSpeed
        self.freq = freq
        self.signal = signal


class ProtOld802_11(WifiStandard):
    '''Class for standard 802.11'''
    numDev = 0

    def __init__(self, device):
        super().__init__(2, [2.4], ['FHSS', 'DSSS'])
        self.device = device
        ProtOld802_11.numDev += 1


class Prot802_11a(WifiStandard):
    '''Class for standard 802.11a'''
    numDev = 0

    def __init__(self, device):
        super().__init__(54, [5], ['OFDM'])
        self.device = device
        Prot802_11a.numDev += 1


class Prot802_11b(WifiStandard):
    '''Class for standard 802.11b'''
    numDev = 0

    def __init__(self, device):
        super().__init__(11, [2.4], ['HR-DSSS'])
        self.device = device
        Prot802_11b.numDev += 1


class Prot802_11g(WifiStandard):
    '''Class for standard 802.11g'''
    numDev = 0

    def __init__(self, device):
        super().__init__(54, [2.4], ['OFDM'])
        self.device = device
        Prot802_11g.numDev += 1


class Prot802_11n(WifiStandard):
    '''Class for standard 802.11n'''
    numDev = 0

    def __init__(self, device):
        super().__init__(600, [2.4, 5], ['OFDM'])
        self.device = device
        Prot802_11n.numDev += 1


class Prot802_11ac(WifiStandard):
    '''Class for standard 802.11ac'''
    numDev = 0
    def __init__(self, device):
        super().__init__(1300, [5], ['256-QAM'])
        self.device = device
        Prot802_11ac.numDev += 1


if __name__ == '__main__':
    prot_1 = ProtOld802_11('THis')
    prot_2 = ProtOld802_11('THis')
    prot_3 = ProtOld802_11('THis')
    print('Frequency of wi-fi for 802.11: ', prot_2.freq)
    print('802.11: ', ProtOld802_11.numDev)

    device11a_1 = Prot802_11a('mobile')
    print('802.11a: ', Prot802_11a.numDev)

    device11b_1 = Prot802_11b('mobile')
    print('802.11b: ', Prot802_11b.numDev)

    device11g_1 = Prot802_11g('laptop')
    device11g_2 = Prot802_11g('camera')
    print('802.11g: ', Prot802_11g.numDev)

    device11n_1 = Prot802_11n('camera1')
    device11n_2 = Prot802_11n('camera2')
    device11n_3 = Prot802_11n('camera3')
    print('802.11n: ', Prot802_11n.numDev)

    print('802.11ac: ', Prot802_11ac.numDev)

print('doc: ', help(Prot802_11ac))