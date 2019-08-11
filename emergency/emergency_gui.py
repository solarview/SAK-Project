import emergency_core
from tkinter import Tk, Label, Button


def start_gui():
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+"+str(window.winfo_screenheight())+"+"+str(window.winfo_screenwidth()))
    window.resizable(False, False)
    window.title('Emergency - SAK')

    emergency_core.call_by_gsm()

    calling_label = Label(window, text="Calling 119",
                          width=10, height=5, relief="solid")
    button = Button(window, overrelief="solid", text="Call Off 119", width=15,
                            command=call_off, repeatdelay=1000, repeatinterval=100)
    calling_label.pack()
    button.pack()

def call_off(event):
    emergency_core.call_off()