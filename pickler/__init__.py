'''Module to save and load data to file'''
import pickle
import os


def create_directories(file_path):
    '''Creates necesesary directories'''
    os.makedirs(os.path.dirname(file_path), exist_ok=True)


def save_state(file_path, state):
    '''Saves state to a file'''
    file_path = os.path.expanduser(file_path)
    create_directories(file_path)
    with open(file_path, 'wb') as file:
        pickle.dump(state, file)


def load_state(file_path):
    '''Loads generations data from a file'''
    file_path = os.path.expanduser(file_path)
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        return None
