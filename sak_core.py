import os
from tkinter import Toplevel, Canvas, PhotoImage, CENTER, NW, N, NE, SW, S, SE, Label
import math
from PIL import Image, ImageTk
 

import medicine
import treatment
import cprhelper as cpr
import heartbeat
import emergency


NUMBER_OF_MEDICINE_CONTAINER = 6
NUMBER_OF_IMAGE_BUTTON = 0
RESOURCE_DIR_PATH = os.path.dirname(
    os.path.realpath(__file__)) + "\\" + "resources" + "\\"

def start_sak_main_window():
    global NUMBER_OF_IMAGE_BUTTON
    NUMBER_OF_IMAGE_BUTTON = 0
    window = Toplevel()
    window.geometry(str(window.winfo_screenwidth()) +
                    "x" + str(window.winfo_screenheight()))
    window.title('SAK - Smart Aid Kit')
    for (name, func) in [("treatment_logo", treatment.start_gui), ("medicine_logo", medicine.start_list_gui), ("emergency_logo", emergency.start_gui), ("cpr_logo", cpr.start_gui),
                         ("heartbeat_logo", heartbeat.start_gui)]:
        create_image_button(window, name, func)
    
    window.mainloop()


def create_image_button(window: Toplevel, name: str, func) -> Canvas:
    side_size = int(window.winfo_screenheight() / 9)
    ima = Image.open(RESOURCE_DIR_PATH + "images\\" + name + ".png")
    ima = ima.resize((side_size, side_size,), Image.ANTIALIAS)
    ima = ImageTk.PhotoImage(ima)
    label = Label(window, image=ima)
    label.place(width=side_size, height=side_size)
    label.image = ima
    label.bind("<Button-1>", lambda event: func())
    label.pack_configure(anchor=CENTER)
