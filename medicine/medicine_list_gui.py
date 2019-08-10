import os
import sys
from tkinter import Canvas, Tk
import math
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import medicine_core as med
import medicine_info_gui as minfo


NUMBER_OF_IMAGE_BUTTON = 0


def start_gui():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "+0+0")
    window.title('Medicine List SAK')
    window.resizable(False, False)

    canvas = Canvas(window, height=window.winfo_screenheight(),
                    width=window.winfo_screenwidth(), relief="solid", bd=2)

    medicines = med.get_medicines()
    for medicine in medicines:
        create_medicine_as_button(canvas, window, medicine)

    canvas.pack()
    window.mainloop()


def create_medicine_as_button(canvas: Canvas, window: Tk, medicine):  # TODO
    global NUMBER_OF_IMAGE_BUTTON
    NUMBER_OF_IMAGE_BUTTON += 1

    i = NUMBER_OF_IMAGE_BUTTON % 4
    if NUMBER_OF_IMAGE_BUTTON % 4 == 0:
        i = 4

    x = window.winfo_screenwidth() * i / 5
    y = window.winfo_screenheight() * math.ceil(NUMBER_OF_IMAGE_BUTTON / 3) / 3
    side_size = window.winfo_screenheigh() / 8
    rec_id = canvas.create_rectangle(x - side_size / 2, y - side_size / 2,
                                     x + side_size / 2, y + side_size / 2, fill="blue", tags = str(medicine[0]))
    rec_text = ""
    if medicine[2] == 1:
        rec_text = medicine[1]
    else:
        rec_text = "Empty"
    canvas.create_text(x, y, Text=rec_text)
    canvas.tag_bind(rec_id, "<Button-1>", button_clicked)


def button_clicked(event):
    medicines = med.get_medicines()
    for medicine in medicines:
        if str(medicine[0]) == event.widget.find_withtag("current"):
            minfo.start_gui(medicine)
