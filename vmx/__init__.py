'''Vmx file editor module'''


def read_vmx(vmx_path):
    '''Converts a vmx file into dictionary format'''
    data = {}
    with open(vmx_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip().split(' = ')
            data[line[0]] = line[1].lstrip('"').rstrip('"')
    return data


def write_vmx(vmx_path, data):
    '''Converts a dictionary to vmx file'''
    with open(vmx_path, 'w') as file:
        for key, value in data.items():
            file.write(f'{key} = "{value}"\n')
