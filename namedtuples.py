'''Stores the namedtuples of the script'''
import collections

Attributes = collections.namedtuple('Attributes', [
    'mother_vm',
    'output_dir',
    'starting_vm',
    'ending_vm',
    'guest_username',
    'guest_password',
])
