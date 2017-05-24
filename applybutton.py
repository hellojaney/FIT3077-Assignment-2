from Tkinter import *

"""
The apply button applies the selected option in the dropdown boxes.
"""

class ApplyButton:
    def __init__(self, guiFrame, caller, column):
        self.caller = caller
        self.button = Button(guiFrame, text = "Apply", command = self.applyOptions)
        self.button.grid(row = 0, column = column)


    def applyOptions(self):
        self.caller.applyOptions()