class Connection_with_user():
    def command_for_get_data(self):
        command_task = input('Enter command: 1 - write to file, 2 - write to console, '
                             '3 - write to file and console: ')
        if command_task == '1' or command_task == '3':
            file_name = input('Enter file name: ')
            return(command_task, file_name)
        else: return(command_task)