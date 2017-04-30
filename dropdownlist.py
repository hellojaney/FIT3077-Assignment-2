import Tkinter as tk

class DropDownList():
    def __init__(self, guiFrame, inactiveLocations, caller):
        self.caller = caller
        self.inactiveList = inactiveLocations
        self.inactiveList.insert(0, "--- Select a Location ---")
        self.dropVar = tk.StringVar()
        self.dropVar.set("--- Select a Location ---")
        self.dropMenu = tk.OptionMenu(guiFrame, self.dropVar, *self.inactiveList, command=self.selectOption)
        self.dropMenu.grid(row = 0, column = 0)

    def selectOption(self, option):
        if option == "--- Select a Location ---":
            return
        self.caller.makeLocationActive(option)
