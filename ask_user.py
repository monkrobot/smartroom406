'''This module for connection with user'''


class ConnectionWithUser:
    '''
    This class asks user to print data to console or to save it
    devices.py class Devices - child
    '''

    @staticmethod
    def command_for_get_data():
        '''
        Asks user to print data to console or to save it
        :return: Task to write_and_save_data_from_devices and file name,
        which use to save data
        '''
        command_task = input('Enter command: 1 - write to file, 2 - write to console, '
                             '3 - write to file and console: ')
        if command_task == '1' or command_task == '3':
            file_name = input('Enter file name: ')
            return command_task, file_name
        return command_task
