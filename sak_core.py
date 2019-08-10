import os
from tkinter import *

import math

import medicine.medicine_list_gui as medicine
import treatment.treatment_gui as treatment

NUMBER_OF_MEDICINE_CONTAINER = 8
NUMBER_OF_IMAGE_BUTTON = 0
RESOURCE_DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + "resources/"


def start_sak_main_window():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" + str(window.winfo_screenheight()))
    window.title('SAK - Smart Aid Kit')
    canvas = Canvas(window, height=window.winfo_screenheight(), width=window.winfo_screenwidth(), relief="solid", bd=2)

    for (name, func) in [("treatment_logo", treatment_callback), ("medicine_logo", medicine_callback),
                         ("emergency_logo", emergency_callback), ("CPR_logo", cpr_callback),
                         ("heartbeat_logo", heartbeat_callback)]:
        im = create_image_button(canvas, window, name)
        im.bind("<Button-1>", func)

    canvas.focus_set()
    canvas.pack()
    window.pack()


def create_image_button(canvas: Canvas, window: Tk, name: str) -> Canvas:
    global NUMBER_OF_IMAGE_BUTTON
    NUMBER_OF_IMAGE_BUTTON += 1
    ima = PhotoImage(RESOURCE_DIR_PATH + "images/" + name + ".png")
    ima.zoom(window.winfo_screenheight() / (6 * ima.height()), window.winfo_screenheight() / (6 * ima.height()))
    i = NUMBER_OF_IMAGE_BUTTON % 3
    if NUMBER_OF_IMAGE_BUTTON % 3 == 0:
        i = 3
    return canvas.create_image(window.winfo_screenwidth() * i / 4,
                               window.winfo_screenheight() * math.ceil(NUMBER_OF_IMAGE_BUTTON / 3) / 3, image=ima,
        anchor=CENTER)


def treatment_callback():
    treatment.start()


def medicine_callback():
    medicine.start_gui()


def emergency_callback():  # TODO
    pass


def cpr_callback():  # TODO
    pass


def heartbeat_callback():  # TODO
    pass
