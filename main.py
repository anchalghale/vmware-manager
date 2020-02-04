'''Main script'''
import os
import threading

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askinteger, askstring

import pygubu
from vmrun import Vmrun

from builder import Builder
from logger import TkinterLogger
from namedtuples import Attributes
from pickler import load_state, save_state

VMRUN = 'C:/Program Files (x86)/VMware/VMware Workstation/vmrun.exe'


class Application:
    '''The gui class of the application'''

    def __init__(self, root):
        self.root = root
        builder = pygubu.Builder()
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)
        builder.connect_callbacks(self)
        self.root.title('VMware Manager')
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
        self.builder.set_entry('guest_username', self.attributes.guest_username)
        self.builder.set_entry('guest_password', self.attributes.guest_password)

    def set_attributes(self):
        '''Sets the attributes for batch processing'''
        attributes = []
        attributes.append(askopenfilename(title='Select mother VM', filetypes=['Vmx *.vmx']))
        attributes.append(askdirectory(title='Select output directory for VMs'))
        attributes.append(askinteger('Enter an integer', 'Starting VM'))
        attributes.append(askinteger('Enter an integer', 'Ending VM'))
        attributes.append(askstring('Enter a string', 'Guest Username'))
        attributes.append(askstring('Enter a string', 'Guest Password'))

        self.attributes = Attributes(*attributes)
        save_state('~/vmware-manager-state', self.attributes)
        self.update_gui()

    def clean_vms(self):
        '''Cleans all the vms in a folder'''
        self.logger.log('Cleaning VMs...')
        os.removedirs(self.attributes.output_dir)

    def clone_vms(self):
        '''Clones all the vms in a folder'''
        self.logger.log('Cloning VMs...')

    def stop_vm(self, vmx, mode='soft'):
        '''Stops a vm'''
        self.logger.log(f'Stopping {os.path.basename(vmx)}..., mode={mode}')
        virutal_machine = Vmrun(vmx=self.attributes.mother_vm,
                                user=self.attributes.guest_username,
                                password=self.attributes.guest_password,
                                debug=True,
                                vmrun=VMRUN)
        virutal_machine.stop(mode)

    def stop_vms(self, mode='soft'):
        '''Stops all the vms'''
        def task():
            self.stop_vm(self.attributes.mother_vm, mode)
            self.builder.enable_all(self.root)
        self.builder.disable_all(self.root)
        threading.Thread(target=task, daemon=True).start()

    def stop_vms_soft(self):
        '''Stops all the vms mode=soft'''
        self.stop_vms(mode='soft')

    def stop_vms_hard(self):
        '''Stops all the vms mode=hard'''
        self.stop_vms(mode='hard')


def main():
    '''Main function of the script'''
    root = Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
