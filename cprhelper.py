from tkinter import Tk, Label
import sak_gpio

window = None


def start_gui():
    global window
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+0+0")
    window.resizable(False, False)
    window.title('CPR Helper - SAK')

    met_label = Label(window, text="100 / 60s", font=("Purisa", 30), anchor="center")
    met_label.pack()
    beep_repeat()

    window.mainloop()


def beep_repeat():
    global window
    make_beep_sound()
    window.after(int(600), beep_repeat)


def make_beep_sound():
    sak_gpio.out_beep_sound(1)
