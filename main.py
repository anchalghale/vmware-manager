
import os
import subprocess
import time
import sys

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger


import pygubu


# Tk().withdraw()
# MOTHER_VM = askopenfilename()
# if not MOTHER_VM:
#     sys.exit()

# START = askinteger('Enter an integer', 'Starting worker')
# if not START:
#     sys.exit()
# END = askinteger('Enter an integer', 'Ending worker')
# if not END:
#     sys.exit()

class Application:
    def __init__(self, root):

        # 1: Create a builder
        self.builder = builder = pygubu.Builder()
        root.title('VMware Manager')
        builder.add_from_file('mainframe.ui')
        builder.get_object('main_frame', root)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
