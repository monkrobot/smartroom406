import serial

class Com_comunication():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_data(self):
        read_data = serial.Serial(self.name, self.speed)
        # If you to continue file 'output_from_', not to rewrite it, then you must to change 'w' to 'a'
        file_com = open('output_from_' + str(self.name) +'.txt', 'w')
        i = 0
        while True:
            data_sensor = str(read_data.readline())
            print(i, data_sensor)
            file_com.write(data_sensor + '\n')
            i += 1
        file_com.close()

    def set_data(self, data):
        write_data = serial.Serial(self.name, self.speed)
        write_data.write(data)

com_comunication = Com_comunication('COM3', 9600)
com_comunication.get_data()
# Prefix 'b' converted data to bytes
com_comunication.set_data(b'5')