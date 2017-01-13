import serial

class Com_comunication():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_data(self):
        read_data = serial.Serial(self.name, self.speed)
        # If you want to continue file 'output_from_', not to rewrite it, then you must change 'w' to 'a'
        file_com = open('output_from_' + str(self.name) +'.txt', 'w')
        file_com.write('Data from ' + str(self.name) + '\n')
        file_com.close()
        while True:
            data_sensor = str(read_data.readline())
            print(data_sensor)
            file_com = open('output_from_' + str(self.name) + '.txt', 'a')
            file_com.write(data_sensor + '\n')
            file_com.close()

    def set_data(self, data):
        write_data = serial.Serial(self.name, self.speed)
        write_data.write(data)

def inner_function()

com_comunication = Com_comunication('COM3', 9600)
com_comunication.get_data()
# Prefix 'b' converted data to bytes
com_comunication.set_data(b'5')

