''' Module that contains the the utility functions of gui '''
import tkinter as tk
import datetime


class Logger:
    ''' Base logger class '''

    def __init__(self, log_format):
        self.log_format = log_format

    def set_entry(self, name, value):
        ''' Sets value of entry component '''
        raise NotImplementedError

    def log(self, message, console):
        ''' Logs a message to the console with time '''
        raise NotImplementedError


class CliLogger(Logger):
    ''' A cli logger '''

    def __init__(self, log_format='%H:%M:%S', ignore_entries=False):
        Logger.__init__(self, log_format)
        self.ignore_entries = ignore_entries

    def set_entry(self, name, value):
        ''' Sets value of entry component '''
        if not self.ignore_entries:
            print(f'{name} -> {value}')

    def log(self, message, console=None):
        ''' Logs a message to the console including time '''
        print(f'{datetime.datetime.now().strftime(self.log_format)} - {str(message)}')


class TkinterLogger(Logger):
    ''' A wrapper class around the pygubu builder for easy gui building '''

    def __init__(self, builder, log_format='%H:%M:%S'):
        self.builder = builder
        Logger.__init__(self, log_format)

    def widget_exists(self, name):
        ''' Checks if a widget exists '''
        return name in self.builder.objects

    def set_entry(self, name, value):
        ''' Sets value of entry component '''
        try:
            if self.widget_exists(name):
                self.builder.get_object(name).delete(0, tk.END)
                self.builder.get_object(name).insert(0, str(value))
        except RuntimeError:  # temporary fix
            pass

    def write_line(self, name, value):
        ''' Writes a line to a textbox '''
        try:
            self.builder.get_object(name).insert(tk.END, '>> ' + str(value) + '\n')
            self.builder.get_object(name).see('end')
        except RuntimeError:  # temporary fix
            pass

    def log(self, message, console='console'):
        ''' Logs a message to the console including time '''
        self.write_line(
            console, f'{datetime.datetime.now().strftime(self.log_format)} - {str(message)}')
