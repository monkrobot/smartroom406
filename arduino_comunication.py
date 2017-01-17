import serial

import connection_with_user

# class for comunication with com-port
class Com_comunication():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    #function for read data from com-port
    def get_data(self, inner_function, connection_with_user):

        inner_function(self.name, self.speed, connection_with_user)

    #function for writing data to com-port
    def set_data(self, data):
        write_data = serial.Serial(self.name, self.speed)
        write_data.write(data)

# inner-function for function get-data in class com_comunication
def print_function(name, speed, command_for_get_data):
    #command_for_get_data - data from function command_for_get_data
    #in file connection_with_user.py
    data_from_command_for_get_data = command_for_get_data()
    read_data = serial.Serial(name, speed)
    if data_from_command_for_get_data[0] == '1' or data_from_command_for_get_data[0] == '3':
        # If you want to continue file 'output_from_', not to rewrite it, then you must change 'w' to 'a'
        file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'w')
        file_com.write('Data from ' + str(name) + '\n')
        if data_from_command_for_get_data[0] == '3':
            while True:
                data_sensor = str(read_data.readline())
                print(data_sensor)
                file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
                file_com.write(data_sensor + '\n')
                file_com.close()
        else:
            while True:
                data_sensor = str(read_data.readline())
                file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
                file_com.write(data_sensor + '\n')
                file_com.close()
    elif data_from_command_for_get_data[0] == '2':
        while True:
            data_sensor = str(read_data.readline())
            print(data_sensor)
    else:
        print('Error')

com_comunication = Com_comunication('COM3', 9600)
com_comunication.get_data(print_function, connection_with_user.command_for_get_data)

## Prefix 'b' converted data to bytes
#com_comunication.set_data(b'5')