#import serial
#
import connection_with_user

# inner-function for function get-data in class com_comunication
def print_function(name, command_for_get_data, data):
    #command_for_get_data - data from function command_for_get_data
    #in file connection_with_user.py
    data_from_command_for_get_data = command_for_get_data()
    if data_from_command_for_get_data[0] == '1' or data_from_command_for_get_data[0] == '3':
        # If you want to continue file 'output_from_', not to rewrite it, then you must change 'w' to 'a'
        file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'w')
        file_com.write('Processed data from ' + str(name) + '\n')
        if data_from_command_for_get_data[0] == '3':
            print(data)
            file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
            file_com.write(data + '\n')
            file_com.close()
        else:
                print(data)
                file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
                file_com.write(data + '\n')
                file_com.close()
    elif data_from_command_for_get_data[0] == '2':
        print(data)
    else:
        print('Error')

#print_function('COM3', connection_with_user.command_for_get_data, data)