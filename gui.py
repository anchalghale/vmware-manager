'''The gui class of the application'''
import os

from tkinter.filedialog import askdirectory, askopenfilename

import pygubu

from builder import Builder
from logger import TkinterLogger
from pickler import load_state, save_state


from namedtuples import Attributes


class Gui:
    '''The gui class of the application'''

    def __init__(self, root):
        self.root = root
        builder = pygubu.Builder()
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)
        builder.connect_callbacks(self)
        root.protocol("WM_DELETE_WINDOW", self.on_closing)
        root.title('VMware Manager')
        root.wm_attributes("-topmost", 1)
        self.builder = Builder(builder)
        self.logger = TkinterLogger(builder)

        self.set_attributes(load_state('~/vmware-manager-state'))

    def update_gui(self, attributes):
        '''Updates the gui components'''
        for field in attributes._fields:
            self.builder.set_variable(field, getattr(attributes, field))

    def on_closing(self):
        ''' Callback for on closing event '''
        save_state('~/vmware-manager-state', self.get_attributes())
        self.root.destroy()

    def get_attributes(self):
        '''Returns an attribute class from gui value'''
        obj = {field: self.builder.get_variable(field) for field in Attributes._fields}
        return Attributes(**obj)

    def set_vm(self, label, index):
        '''Sets a mother_vm attribute'''
        path = os.path.realpath(askopenfilename(
            title=f'Select {label} VM {index}', filetypes=['Vmx *.vmx']))
        self.builder.set_variable(f'{label}_vm{index}', path)

    def set_mother_vm1(self):
        '''Sets a mother_vm1 attribute'''
        self.set_vm('mother', 1)

    def set_mother_vm2(self):
        '''Sets a mother_vm2 attribute'''
        self.set_vm('mother', 2)

    def set_vpn_vm1(self):
        '''Sets a vpn_vm1 attribute'''
        self.set_vm('vpn', 1)

    def set_vpn_vm2(self):
        '''Sets a vpn_vm2 attribute'''
        self.set_vm('vpn', 2)

    def set_vms(self):
        '''Sets the mother_vms attribute'''
        self.set_vm('mother', 1)
        self.set_vm('mother', 2)
        self.set_vm('vpn', 1)
        self.set_vm('vpn', 2)

    def set_output_dir(self):
        '''Sets the output_dir attribute'''
        output_dir = os.path.realpath(askdirectory(title='Select output directory for VMs'))
        self.builder.set_variable('output_dir', output_dir)

    def set_attributes(self, attributes=None):
        '''Sets the attributes for batch processing'''
        if not attributes:
            self.builder.set_variable('starting_vm1', 1)
            self.builder.set_variable('ending_vm1', 10)
            self.builder.set_variable('starting_vm2', 11)
            self.builder.set_variable('ending_vm2', 20)
            self.builder.set_variable('guest_username', 'John')
            self.builder.set_variable('guest_password', '1234')
            self.set_vms()
            self.set_output_dir()
            attributes = self.get_attributes()
            save_state('~/vmware-manager-state', attributes)
        else:
            self.update_gui(attributes)
