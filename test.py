from Tkinter import *
from inactivelocations import InactiveLocations
from activelocations import ActiveLocations

def addLocation(location):
    if location == "-- Select a Location --":
        print("Not a valid location.")
        return
    inactiveLocations.remove(location)
    menu = dropDownMenu['menu']
    menu.delete(value)


class DropDownList:
    def __init__(self, root, inactiveLocations):
        #create a list of all locations and add "select a location" at the start of the list
        list = inactiveLocations.getAll()
        list.insert(0, "-- Select a Location --")

        #create stringvar and set the "-- Select a Location --" as the default of the menu
        self.var = StringVar(root)
        self.var.set(list[0])
        self.menu = OptionMenu(root, self.var, *list, command = addLocation)
        self.menu.grid(row = 0, column = 0)



import sys

from Tkinter import *

# My frame for form
class simpleform_ap(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.grid()

    def initialize(self):

        # Dropdown Menu
        optionList = ["Yes","No"]
        self.dropVar=StringVar()
        self.dropVar.set("Yes") # default choice
        self.dropMenu1 = OptionMenu(self, self.dropVar, *optionList, command=self.func)
        self.dropMenu1.grid(column=1,row=4)

    def func(self,value):
        print(value)

def create_form(argv):
    form = simpleform_ap(None)
    form.title('My form')
    form.mainloop()

if __name__ == "__main__":
  create_form(sys.argv)