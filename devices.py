'''Read data from Com port, send it to sensor module and print results of processing'''

import mpu9265_module
import com_communication

from ask_user import ConnectionWithUser as ConnectionWithUser
from write_data import WriteAndSaveData as WriteAndSaveData


class Devices(ConnectionWithUser, WriteAndSaveData):
    '''
    This class is inherited from ConnectionWithUser, WriteAndSaveData
    Read data from Com port, send it to sensor module and print results of processing
    '''
    def __init__(self, module, module_name, name='COM3', speed=9600, testing=True):
        self.name = name
        self.speed = speed
        self.module_name = module_name
        self.testing = testing
        self.exec_function = getattr(module, module_name)

    def processing_data(self):
        '''
        Use module com_communication.py for reading data from Com
        Use sensor module for processing data
        Use write_data for print data to console or/and file
        :return: processed data from sensor module
        '''
        if self.testing:
            data = com_communication.ComCommunication(self.name, self.speed).get_data()
            data_sensor = self.exec_function(data)
            self.print_function(self.name, self.command_for_get_data, data_sensor)

test = Devices(mpu9265_module, 'mpu92_65')
# test = Devices(mpu9265_module, 'mpu92_65', 'COM3', 9600, True)

test.processing_data()
print("That's all")
