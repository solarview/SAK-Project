from tkinter import Label, Canvas, Tk
import math
import sak_core
import sqlite3


NUMBER_OF_IMAGE_BUTTON = 0


def start_list_gui():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "+0+0")
    window.title('Medicine List SAK')
    window.resizable(False, False)

    canvas = Canvas(window, height=window.winfo_screenheight(),
                    width=window.winfo_screenwidth(), relief="solid", bd=2)

    medicines = get_medicines()
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
                                     x + side_size / 2, y + side_size / 2, fill="blue", tags=str(medicine[0]))
    rec_text = ""
    if medicine[2] == 1:
        rec_text = medicine[1]
    else:
        rec_text = "Empty"
    canvas.create_text(x, y, Text=rec_text)
    canvas.tag_bind(rec_id, "<Button-1>", button_clicked)


def button_clicked(event):
    medicines = get_medicines()
    for medicine in medicines:
        if str(medicine[0]) == event.widget.find_withtag("current"):
            start_info_gui(medicine)


def start_info_gui(medicine):
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


def start_db():
    conn = sqlite3.connect(sak_core.RESOURCE_DIR_PATH +
                           'medicine.db')  # get medicine data
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='medicine'")  # Table Name is 'medicine'
    rows = cur.fetchall()
    is_exist = False
    for row in rows:
        if row[0] == "medicine":
            is_exist = True
    if not is_exist:  # If Table is not exist, we will create table
        cur.execute("CREATE TABLE "
                    "medicine("
                    "id INTEGER NOT NULL,"
                    "name TEXT, "
                    "is_exist INTEGER DEFAULT 0 NOT NULL)"
                    )  # medicine(id, name, is_exist)
        for i in range(1, sak_core.NUMBER_OF_MEDICINE_CONTAINER):
            cur.execute("INSERT INTO medicine(id) VALUES (?)", [i])


def get_medicines():
    conn = sqlite3.connect('../resources/medicine.db')  # get medicine data
    cur = conn.cursor()
    cur.execute("SELECT id, name, is_exist FROM medicine")
    rows = cur.fetchall()
    conn.close()
    return rows


def is_medicine_exist(medicine_id: int) -> int:  # TODO use RPi.GPIO, return 0 or 1
    return 0


def turn_on_led(medicine_id: int):  # TODO use RPI.GPIO, only for a sec
    pass


def register_medicine(medicine_id: int, name: str):
    conn = sqlite3.connect('../resources/medicine.db')  # get medicine data
    cur = conn.cursor()
    cur.execute("UPDATE medicine SET name = ?, is_exist = ? WHERE id = ?",
                [name, is_medicine_exist(medicine_id), medicine_id])
    conn.close()
