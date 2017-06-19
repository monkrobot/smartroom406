import mpu9265_module
import com_communication

from connection_with_user import Connection_with_user as Connection_with_user
from write_and_save_data_from_devices_module import Write_and_save_data as Write_and_save_data

# - writing_of_processed_data = write_and_save_data_from_devices_module.print_function

# - data_from_com = com_comunication.Com_comunication('COM3', 9600)
#data = data_from_com.get_data(writing_of_processed_data, connection_with_user.command_for_get_data)

class Devices(Connection_with_user, Write_and_save_data):
    def __init__(self, name, speed, module, module_name, testing):
        self.name = name
        self.speed = speed
        self.module_name = module_name
        self.testing = testing
        self.exec_function = getattr(module, module_name)
    def processing_data(self):
        if self.testing == True:
            data = com_communication.Com_communication(self.name, self.speed).get_data()
            data_sensor = self.exec_function(data)
            self.print_function(self.name, self.command_for_get_data, data_sensor)

a_test = Devices('COM3', 9600, mpu9265_module, 'mpu92_65', True)

a_test.processing_data()
print("That's all")
