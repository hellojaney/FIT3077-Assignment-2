from Tkinter import *

def closeMonitor(frame):
    frame.pack_forget()
    frame.destroy()

class WeatherFrame:
    def __init__(self, root, list):
        self.frame = Frame(root)
        self.frame.pack(side=TOP, anchor=NW)

        self.label = Label(self.frame, text="%s" % list[0], font="Helvetica 16 bold")
        self.label1 = Label(self.frame, text="Updated at: %s" % list[1], font="Helvetica 14")
        self.label2 = Label(self.frame, text="Temperature: %sC" % list[2], font="Helvetica 14")
        self.label3 = Label(self.frame, text="Rainfall: %smm" % list[3], font="Helvetica 14")
        self.closeButton = Button(self.frame, text="x", command=lambda: closeMonitor(self.frame))

        self.label.grid(row=0, column=0)
        self.closeButton.grid(row=0, column=5)
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=2, column=0)
        self.label3.grid(row=3, column=0)

