from tkinter import Label, Canvas, Tk, Listbox
import math
import sqlite3
from sak_setting import RESOURCE_DIR_PATH


def start_list_gui():
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "+0+0")
    window.title('Medicine List - SAK')
    window.resizable(False, False)

    if len(get_medicines()) > 0:
        medicine_list = Listbox(
            window, selectmode='extended', yscrollcommand=True)

        for medicine in get_medicines():
            medicine_list.insert(
                medicine[0], "Name: " + medicine[2] + ", Expire_date: " + medicine[3])

        medicine_list.bind("<<ListboxSelect>>", lambda event: start_info_gui(
            int(event.widget.curselection()[0])))
        medicine_list.pack()

    window.mainloop()


def start_info_gui(medicine_id): 
    medicine = get_medicine(medicine_id)
    window = Tk()
    window.geometry(str(int(window.winfo_screenwidth() / 4)) + "x" +
                    str(int(window.winfo_screenheight() / 3)) + "+0+0")
    window.resizable(False, False)
    window.title(str(medicine[2]) + ' - Medicines List SAK')

    name_label = Label(window, text="Name : " +
                       str(medicine[2]), width=10, height=3, relief="solid")
    expire_date_label = Label(window, text="Expire date : " +
                              str(medicine[3]), width=10, height=3, relief="solid")
    document_label = Label(window, text=str(
        medicine[4]), width=10, height=3, ipady=20, anchor="n", relief="solid", justify="left")

    name_label.pack()
    expire_date_label.pack()
    document_label.pack()
    window.mainloop()


def button_clicked(event):
    w = event.widget
    index = int(event.widget.curselection()[0])
    start_info_gui(index)


def rfid_scan():
    pass


def start_db():
    conn = sqlite3.connect(RESOURCE_DIR_PATH + 'medicine.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='medicine'")  # Table Name is 'medicine'
    rows = cur.fetchall()
    is_exist = False
    for row in rows:
        if row[0] == "medicine":
            is_exist = True
            break
    if not is_exist:  # If Table is not exist, we will create table
        cur.execute("CREATE TABLE "
                    "medicine("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "rfid_id INTEGER NOT NULL,"
                    "name TEXT NOT NULL,"
                    "expire_date TEXT NOT NULL,"
                    "document TEXT,"
                    "now_exist INTEGER DEFAULT 1 NOT NULL)"
                    )
    conn.commit()
    conn.close()


def get_medicines():
    conn = sqlite3.connect(RESOURCE_DIR_PATH +
                           'medicine.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT id, rfid_id, name, expire_date, document, now_exist FROM medicine")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_medicine(medicine_id: int):
    conn = sqlite3.connect(RESOURCE_DIR_PATH +
                           'medicine.db')
    cur = conn.cursor()
    cur.execute("SELECT id, rfid_id, name, expire_date, document, now_exist FROM medicine WHERE id = ?", [
                medicine_id])
    rows = cur.fetchall()
    conn.close()
    return rows[0]


def register_medicine(name: str, expire_date: str, rfid_id: int):
    conn = sqlite3.connect(RESOURCE_DIR_PATH +
                           'medicine.db')  # get medicine data
    cur = conn.cursor()
    cur.execute("INSERT INTO medicine(rfid_id, name, expire_date) VALUES (?, ?, ?)", [
                rfid_id, name, expire_date])
    conn.commit()
    conn.close()
