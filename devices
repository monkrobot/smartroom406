import devices_modules

class Devices():
    def processing_data(self, information):
        #information = input('Enter name of function: ')
        exec_function = getattr(devices_modules, information)
        exec_function()
a = Devices()
a.processing_data('mpu92_65')