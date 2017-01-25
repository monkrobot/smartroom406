import devices_modules
import arduino_comunication
import connection_with_user
import write_and_save_data_from_devices_module

writing_of_processed_data = write_and_save_data_from_devices_module.print_function

data_from_com = arduino_comunication.Com_comunication('COM3', 9600)
#data = data_from_com.get_data(writing_of_processed_data, connection_with_user.command_for_get_data)

class Devices():
    def __init__(self, name, command_for_get_data, module_name, data, testing, writing_of_processed_data):
        self.name = name
        self.command_for_get_data = command_for_get_data
        self.module_name = module_name
        self.data = data
        self.testing = testing
        self.exec_function = getattr(devices_modules, module_name)
        self.writing_of_processed_data = writing_of_processed_data
    def processing_data(self):
        if self.testing == True:
            self.writing_of_processed_data(self.name, self.command_for_get_data, self.exec_function(self.data))


a = Devices('COM3', connection_with_user.command_for_get_data, 'mpu92_65',
             data_from_com.get_data(writing_of_processed_data, connection_with_user.command_for_get_data),
             True, writing_of_processed_data)
a.processing_data()
print("That's all")