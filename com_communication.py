'''This module for reading and setting data to the Com port'''
import serial

# class for com_communication with com-port
class Com_communication():
    '''Class for reading data from Com port'''
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_data(self):
        '''Special function for reading data from Com port'''
        read_data = serial.Serial(self.name, self.speed)
        while True:
            data_sensor = str(read_data.readline())
            if len(data_sensor) < 30:
                continue
            else:
                print("This is read data" + str(data_sensor))
                # - n = self.print_function(self.name, self.command_for_get_data, data_sensor)
                return data_sensor

    # function for writing data to com-port
    def set_data(self, data):
        '''Special function for setting data to the Com port'''
        write_data = serial.Serial(self.name, self.speed)
        write_data.write(data)


if __name__ == '__main__':
    com_communication = Com_communication('COM3', 9600)
    com_communication.get_data()

## Prefix 'b' converted data to bytes
# com_communication.set_data(b'5')
