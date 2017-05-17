import Tkinter as tk

"""
Code derived from: http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
Creates a custom Tkinter GUI that allows scrolling of information added to it.
"""

class GUI:
    def __init__(self, title):
        # Configure Frame
        self.root = tk.Tk()
        self.root.minsize(width = 300, height = 600)
        self.root.title(title)
        self.canvas = tk.Canvas(self.root, borderwidth = 0, background = "#ffffff")
        self.frame = tk.Frame(self.canvas, background = "#ffffff")

        # Configure Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side = "right", fill = "y")
        self.canvas.pack(side = "left", fill = "both", expand = True)
        self.canvas.create_window((4, 4), window = self.frame, anchor = "nw",tags = "self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)


    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    """
    Initialising the GUI start loop
    """
    def startLoop(self):
        self.root.mainloop()