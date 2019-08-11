import heartbeat_core
from datetime import datetime
from Tkinter import Tk, TOP, BOTH
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('TkAgg')


heartbeat_history = {}
dataplot = None
pplot = None


def start_gui():
    global dataplot, pplot
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+" + str(window.winfo_screenwidth()) + "+0")
    window.resizable(False, False)
    window.title('Heartbeat Monitor - SAK')

    fig = Figure(figsize=(5, 5), dpi=100)
    pplot = fig.add_subplot(111)

    dataplot = FigureCanvasTkAgg(fig, master=window)
    dataplot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    show_heartbeat()

    window.mainloop()


def show_heartbeat():
    global heartbeat_history, dataplot, pplot

    heartbeat_history[datetime.now().strftime(
        "%H:%M:%S")] = heartbeat_core.getHeartBeat()

    pplot.plot(heartbeat_history.keys, heartbeat_history.values)
    dataplot.draw()
    pplot.clear()

    dataplot.get_tk_widget().after(1000 * 1, show_heartbeat)
