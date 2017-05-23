from Tkinter import *

class ApplyButton:
    def __init__(self, guiFrame, caller, column):
        self.caller = caller
        self.button = Button(guiFrame, text = "Apply", command = self.applyOptions)
        self.button.grid(row = 0, column = column)


    def applyOptions(self):
        self.caller.applyOptions()