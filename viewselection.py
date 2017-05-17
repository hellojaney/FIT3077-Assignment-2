import Tkinter as tk

"""
ViewSelection class holds the options to either view Temperature, Rainfall or Both.
"""

class ViewSelection():
    def __init__(self, guiFrame, caller):
        self.caller = caller
        self.viewingOptions = ["Temperature", "Rainfall", "Temperature and Rainfall"]
        self.viewingOptions.insert(0, "--- Viewing Location ---")
        self.dropVar = tk.StringVar()
        self.dropVar.set("--- Select Viewing Option ---")
        self.dropMenu = tk.OptionMenu(guiFrame, self.dropVar, *self.viewingOptions, command=self.selectOption)
        self.dropMenu.grid(row = 0, column = 0)


    """
    Sets the viewing option when an option is selected.
    """
    def selectOption(self, option):
        if option == "--- Select Viewing Option ---":
            return
        self.caller.setViewingOption(option)