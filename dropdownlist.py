from inactivelocations import InactiveLocations
from Tkinter import *

"""
Derived from: http://stackoverflow.com/questions/35132221/python-tkinter-optionmenu-how-to-get-the-selected-choice
"""

class DropDownList(Tk):
    def __init__(self, root, inactiveLocations):
        Tk.__init__(self)
        self.frame = Frame(root)
        self.options = inactiveLocations
        self.initialize()
        self.grid()

    def initialize(self):
        self.dropVar = StringVar()
        self.dropMenu = OptionMenu(self, self.dropVar, *self.options, command=self.selectOption)
        self.dropMenu.grid(column=1, row=4)

    # so far selectOption only prints the value to screen next steps see below
    def selectOption(self,value):
        print(value)
        # remove selection from inactive locations
        # display weather frame for selected location
