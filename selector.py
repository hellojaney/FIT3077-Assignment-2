import Tkinter as tk
"""
LocationSelector class holds and displays the location options that the user selects to view.
"""

class Selector:
    def __init__(self, guiFrame, optionsList, caller, selectorType, column):
        self.selectorType = selectorType
        self.caller = caller
        self.dropVar = tk.StringVar()
        self.optionsList = optionsList
        self.dropVar = tk.StringVar()
        self.dropVar.set(self.optionsList[0])
        self.dropMenu = tk.OptionMenu(guiFrame, self.dropVar, *self.optionsList, command=self.selectOption)
        self.dropMenu.grid(row = 0, column = column)


    """
    Activates location when user selects a location option to view
    """
    def selectOption(self, option):
        if option == self.optionsList[0]:
            option = None
        self.caller.setSelectorValues(option, self.selectorType)