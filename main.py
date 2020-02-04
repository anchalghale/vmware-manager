'''Main script'''
import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askinteger

import pygubu
import vmrun

from builder import Builder
from logger import TkinterLogger
from namedtuples import Attributes
from pickler import load_state, save_state


class Application:
    '''The gui class of the application'''

    def __init__(self, root):
        builder = pygubu.Builder()
        root.title('VMware Manager')
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)
        builder.connect_callbacks(self)

        self.builder = Builder(builder)
        self.logger = TkinterLogger(builder)

        self.attributes = load_state('~/vmware-manager-state')

        if self.attributes:
            self.update_gui()
        else:
            self.set_attributes()

    def update_gui(self):
        '''Updates the gui components'''
        self.builder.set_entry('mother_vm', self.attributes.mother_vm)
        self.builder.set_entry('output_dir', self.attributes.output_dir)
        self.builder.set_entry('starting_vm', self.attributes.starting_vm)
        self.builder.set_entry('ending_vm', self.attributes.ending_vm)

    def set_attributes(self):
        '''Sets the attributes for batch processing'''
        attributes = []
        attributes.append(askopenfilename(title='Select mother VM', filetypes=['Vmx *.vmx']))
        attributes.append(askdirectory(title='Select output directory for VMs'))
        attributes.append(askinteger('Enter an integer', 'Starting VM'))
        attributes.append(askinteger('Enter an integer', 'Ending VM'))

        self.attributes = Attributes(*attributes)
        save_state('~/vmware-manager-state', self.attributes)
        self.update_gui()

    def clean_vms(self):
        '''Cleans all the vms in a folder'''
        self.logger.log('Cleaning VMs...')
        if self.attributes.output_dir:
            os.removedirs(self.attributes.output_dir)


def main():
    '''Main function of the script'''
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
