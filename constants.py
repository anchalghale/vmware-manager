'''Stores the constant variables of the bot'''
import os

DEFAULTS = {
    'starting_vm1': 1,
    'ending_vm1': 10,
    'starting_vm2': 11,
    'ending_vm2': 20,
    'guest_username': 'John',
    'guest_password': '1234',
    'server_name': os.environ['COMPUTERNAME'],
    'start_vms_on_start_up': False,
    'start_vms_periodically': False,
}
