'''This module for writing data to console or save it in file'''


class WriteAndSaveData:
    '''
    Writing data to console or save it in file
    main.py class Devices - child
    '''

    @staticmethod
    def print_function(name, command_for_get_data, data):
        '''Function for writing data to console or save it in file'''

        #command_for_get_data - data from function command_for_get_data
        #in module ask_user.py
        data_from_command_for_get_data = command_for_get_data()
        if data_from_command_for_get_data[0] == '1' or data_from_command_for_get_data[0] == '3':
            # If you want to continue file 'output_from_', not to
            # rewrite it, then you must change 'w' to 'a'
            file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'w')
            file_com.write('Processed data from ' + str(name) + '\n')
            if data_from_command_for_get_data[0] == '3':
                print(data)
                file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
                file_com.write(data + '\n')
                file_com.close()
            else:
                file_com = open(data_from_command_for_get_data[1] + str(name) + '.txt', 'a')
                file_com.write(data + '\n')
                file_com.close()
        elif data_from_command_for_get_data[0] == '2':
            print(data)
        else:
            print('Error')
