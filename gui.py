import Tkinter as tk
from weatherframe import WeatherFrame
from dropdownlist import DropDownList

"""
code heavily reliant upon: http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
creates a custom Tkinter GUI that allows scrolling of information added to it
"""

class GUI(tk.Frame):
    def __init__(self, title, inactive):
        # frame configuration
        self.root = tk.Tk()
        self.root.title(title)
        tk.Frame.__init__(self, self.root)
        self.canvas = tk.Canvas(self.root, borderwidth = 0, background = "#ffffff")
        self.frame = tk.Frame(self.canvas, background = "#ffffff")

        # scrollbar configuration
        self.scrollbar = tk.Scrollbar(self.root, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side = "right", fill = "y")
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.canvas.create_window((4, 4), window = self.frame, anchor = "nw",tags = "self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.optionMenu = DropDownList(self.root,inactive)


    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    # gui startLoop
    def startLoop(self):
        self.root.mainloop()
