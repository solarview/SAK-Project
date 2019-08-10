import math
from tkinter import Label, Tk


def start_gui(medicine):
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+0+0")
    window.resizable(False, False)
    window.title(str(medicine[0]) + ' - Medicine Info SAK')

    rec_text = ""
    is_exist = "True"
    if medicine[2] == 1:
        rec_text = medicine[1]
    else:
        rec_text = "None"
        is_exist = "False"

    name_label = Label(window, text="Name : " + rec_text,
                       width=10, height=5, relief="solid")
    position_label = Label(window, text="Position : " +
                           str(medicine[0]), width=10, height=5, relief="solid")
    is_exist_label = Label(window, text="Is Exist : " +
                           is_exist, width=10, height=5, relief="solid")

    name_label.pack()
    position_label.pack()
    is_exist_label.pack()

    window.mainloop()
