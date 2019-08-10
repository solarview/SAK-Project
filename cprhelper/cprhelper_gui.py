from tkinter import Tk

window = None

def start_gui():
    global window
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+0+0")
    window.resizable(False, False)
    window.title('CPR Helper - SAK')

    #TODO Show Something
    
    beep_repeat()

    window.mainloop()

def beep_repeat():
    global window
    make_beep_sound()
    window.after(1000 * 100 / 60, beep_repeat)

        

def make_beep_sound(): #TODO Use RPi.GPIO or anything else to make beep sound
    pass