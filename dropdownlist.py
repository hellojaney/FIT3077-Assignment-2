from Tkinter import *

class DropDownList(Tk):
    def __init__(self,inactiveLocations):
        Tk.__init__(self)
        self.options = inactiveLocations
        self.initialize()
        self.grid()

    def initialize(self):
        self.dropVar = StringVar()
        self.dropVar.set("--- Select a Location ---")
        self.dropMenu = OptionMenu(self, self.dropVar, *self.options, command=self.selectOption)
        self.dropMenu.grid(column=1, row=4)

    def selectOption(self,value):
        print(value)
        # remove from inactive locations and display