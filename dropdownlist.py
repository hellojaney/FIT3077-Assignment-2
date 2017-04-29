from Tkinter import *
from inactivelocations import InactiveLocations
from activelocations import ActiveLocations


def addLocation(location):
    if location == "-- Select a Location --":
        print("Not a valid location to delete")
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




