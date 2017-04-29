from Tkinter import *


"""
Creates a Frame() for the GUI
Takes a list of information from getAllInfo: location, timestamp, rainfall and temp)
Packs the frame into the GUI
"""

class WeatherFrame:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack(side=TOP, anchor=NW)


    def addData(self, location):
        #create the title and 'x' button, the first item in the list is the location name (title)
        Label(self.frame, text = location.getName(), font ="Helvetica 16 bold").grid(row=0, column=0, sticky = W)
        self.closeButton = Button(self.frame, text="x", command=lambda: self.closeFrame(self.frame)).grid(row = 0, column = 5)

        #weather information
        Label(self.frame, text = "Updated at: " + location.getDateStamp() + ", " + location.getTimeStamp(), font ="Helvetica 14").grid(row=1, column=0, sticky = W)
        Label(self.frame, text = "Temperature: " + str(location.getTemperature()), font="Helvetica 14").grid(row=2, column=0, sticky=W)
        Label(self.frame, text= "Rainfall: " + str(location.getRainfall()), font="Helvetica 14").grid(row=3, column=0, sticky=W)

        #blank label to create spacing
        Label(self.frame, text = " ").grid(row = 4, column = 0)


    def closeFrame(self, frame):
        frame.pack_forget()
        frame.destroy()




    """
    ###### NOT IN USE ANYMORE, DECIDED TO REMOVE ALL FRAMES WHEN REFRESHING ######
    def removeData(self):
        for item in self.frame.winfo_children():
            item.destroy()
    """