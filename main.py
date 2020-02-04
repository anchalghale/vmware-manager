'''Main script'''
import os
import subprocess
import time

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askinteger

import pygubu
import vmrun


class Application:
    '''The gui class of the application'''

    def __init__(self, root):
        self.builder = builder = pygubu.Builder()
        root.title('VMware Manager')
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)
        builder.connect_callbacks(self)

        self.mother_vm = askopenfilename(title='Select mother VM', filetypes=['Vmx *.vmx'])
        self.output_dir = askdirectory(title='Select output directory for VMs')
        self.start = askinteger('Enter an integer', 'Starting worker')
        self.end = askinteger('Enter an integer', 'Ending worker')

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
