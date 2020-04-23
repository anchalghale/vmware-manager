'''Stores the namedtuples of the script'''
import collections

Attributes = collections.namedtuple('Attributes', [
    'mother_vm1',
    'mother_vm2',
    'vpn_vm1',
    'vpn_vm2',
    'output_dir1',
    'output_dir2',
    'starting_vm1',
    'ending_vm1',
    'starting_vm2',
    'ending_vm2',
    'guest_username',
    'guest_password',
    'server_name',
    'start_vms_on_start_up',
    'start_vms_periodically',
])
