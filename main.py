'''Main script'''
import os
import subprocess
import time

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askinteger

import pygubu
import vmrun

from builder import Builder


class Application:
    '''The gui class of the application'''

    def __init__(self, root):
        builder = pygubu.Builder()
        root.title('VMware Manager')
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)
        builder.connect_callbacks(self)

        self.builder = Builder(builder)

        self.mother_vm = askopenfilename(title='Select mother VM', filetypes=['Vmx *.vmx'])
        self.output_dir = askdirectory(title='Select output directory for VMs')
        self.starting_vm = askinteger('Enter an integer', 'Starting VM')
        self.ending_vm = askinteger('Enter an integer', 'Ending VM')

        self.builder.set_entry('mother_vm', self.mother_vm)
        self.builder.set_entry('output_dir', self.output_dir)
        self.builder.set_entry('starting_vm', self.starting_vm)
        self.builder.set_entry('ending_vm', self.ending_vm)

    def clean_vms(self):
        '''Cleans all the vms in a folder'''
        print('hi')


def main():
    '''Main function of the script'''
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
