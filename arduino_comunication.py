import serial

class Com_comunication():
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_data(self, inner_function):
        read_data = serial.Serial(self.name, self.speed)
        inner_function(self.name, read_data)


        # If you want to continue file 'output_from_', not to rewrite it, then you must change 'w' to 'a'
    #    file_com = open('output_from_' + str(self.name) +'.txt', 'w')
    #    file_com.write('Data from ' + str(self.name) + '\n')
#
#
#
    #    while True:
    #        data_sensor = str(read_data.readline())
    #        print(data_sensor)
    #        file_com = open('output_from_' + str(self.name) + '.txt', 'a')
    #        file_com.write(data_sensor + '\n')
    #        file_com.close()
#
    #def set_data(self, data):
    #    write_data = serial.Serial(self.name, self.speed)
    #    write_data.write(data)

def inner_function(name, read_data):
    command_task = input('Enter command: 1 - write to file, 2 - write to console, 3 - write to file and console')
    if command_task == '1' or command_task == '3':
        file_name = input('Enter file name')
        #print(file_name, name)
        # If you want to continue file 'output_from_', not to rewrite it, then you must change 'w' to 'a'
        file_com = open(file_name + str(name) + '.txt', 'w')
        file_com.write('Data from ' + str(name) + '\n')
        if command_task == '3':
            while True:
                data_sensor = str(read_data.readline())
                print(data_sensor)
                file_com = open(file_name + str(name) + '.txt', 'a')
                file_com.write(data_sensor + '\n')
                file_com.close()
        else:
            while True:
                data_sensor = str(read_data.readline())
                file_com = open(file_name + str(name) + '.txt', 'a')
                file_com.write(data_sensor + '\n')
                file_com.close()
    elif command_task == '2':
        while True:
            data_sensor = str(read_data.readline())
            print(data_sensor)
    else:
        print('Error')

com_comunication = Com_comunication('COM3', 9600)
#com_comunication.get_data()
# Prefix 'b' converted data to bytes
com_comunication.get_data(inner_function)