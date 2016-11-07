import GUI
import os
import sys

def __init__(self):
    self.menuBar.addmenuitem('Plugin', 'command',
                             'ValidatorDB',
                             label='ValidatorDB',
                             command=lambda s=self: GUI.MAINWINDOW)
path = os.path.dirname(GUI)
sys.path.append(path)