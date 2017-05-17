from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class GraphWindow:

    def __init__(self, locationName, tempData, rainData, timeList):
        self.tempData = tempData
        self.rainData = rainData
        self.time = timeList
        self.locationName = locationName
        self.openGraph()

    def openGraph(self):
        graphRoot = Tk()
        graphRoot.title('Rainfall and Temperature Graph for ' + self.locationName)
        fig = Figure(figsize=(5,5), dpi=100)
        subplot = fig.add_subplot(111)
        subplot.plot(self.tempData, self.time)
        subplot.plot(self.rainData, self.time)
        subplot.legend(['Temperature', 'Rainfall'], loc='upper left')
        canvas = FigureCanvasTkAgg(fig, graphRoot)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        graphRoot.mainloop()