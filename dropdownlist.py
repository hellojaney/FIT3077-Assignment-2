import Tkinter as tk

"""
DropDownList class holds and displays the location options that the user selects to view.
"""

class DropDownList():
    def __init__(self, guiFrame, inactiveLocations, caller):
        self.caller = caller
        self.inactiveList = inactiveLocations
        self.inactiveList.insert(0, "--- Select a Location ---")
        self.dropVar = tk.StringVar()
        self.dropVar.set("--- Select a Location ---")
        self.dropMenu = tk.OptionMenu(guiFrame, self.dropVar, *self.inactiveList, command=self.selectOption)
        self.dropMenu.grid(row = 0, column = 1)


    """
    Activates location when user selects a location option to view
    """
    def selectOption(self, option):
        if option == "--- Select a Location ---":
            return
        self.caller.createMonitor(option)
