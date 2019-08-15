from serial import Serial
from tkinter import Tk, Label, Button


def start_gui():
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+"+str(window.winfo_screenheight())+"+"+str(window.winfo_screenwidth()))
    window.resizable(False, False)
    window.title('Emergency - SAK')

    call_by_gsm()

    calling_label = Label(window, text="Calling 119",
                          width=10, height=5, relief="solid")
    button = Button(window, overrelief="solid", text="Call Off 119", width=15,
                    command=call_off_event, repeatdelay=1000, repeatinterval=100)
    
    calling_label.pack()
    button.pack()

    window.mainloop()


def call_off_event(event):
    call_off()


serialport = None


def call_by_gsm():
    '''
    global serialport
    serialport = Serial("/dev/ttyAMA0", 115200, timeout=0.5)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATE0\r")
    response = serialport.readlines(None)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    print(response)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATD 119;\r")
    response = serialport.readlines(None)
    '''


def call_off():
    '''
    global serialport
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATH\r")
    response = serialport.readlines(None)
    print(response)
    '''
