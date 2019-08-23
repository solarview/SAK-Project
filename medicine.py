from tkinter import Label, Canvas, Tk, Listbox, Entry, Button, StringVar, Frame, Scrollbar
import math
import sqlite3
from sak_setting import RESOURCE_DIR_PATH
import time
import datetime
import asyncio
from pirc522 import RFID

ids = []


def start_list_gui():
    global ids
    window = Tk()
    window.geometry(str(window.winfo_screenwidth()) + "x" +
                    str(window.winfo_screenheight()) + "+0+0")
    window.title('Medicine List - SAK')
    window.resizable(False, False)

    if len(get_medicines()) > 0:
        medicine_list = Listbox(
            window, selectmode='extended', width=window.winfo_screenwidth(), height=window.winfo_screenheight(), yscrollcommand=True)

        i = 0
        for medicine in get_medicines():
            ids.insert(i, medicine[0])
            medicine_list.insert(
                i, "Name: " + medicine[2] + ", Expire_date: " + medicine[3])
            i += 1
        medicine_list.bind("<<ListboxSelect>>", lambda event: start_info_gui(ids[
            int(event.widget.curselection()[0])]))
        medicine_list.pack()

    window.mainloop()


def start_info_gui(medicine_id):
    medicine = get_medicine_by_id(medicine_id)
    window = Tk()
    window.geometry(str(window.winfo_screenwidth() // 4) + "x" +
                    str(window.winfo_screenheight() // 3) + "+0+0")
    window.resizable(False, False)
    window.title(str(medicine[2]) + ' - Medicines List SAK')

    name_label = Label(window, text="Name : " +
                       str(medicine[2]), width=window.winfo_screenwidth() // 4, height=3, relief="solid")
    expire_date_label = Label(window, text="Expire date : " +
                              str(medicine[3]), width=window.winfo_screenwidth() // 4, height=3, relief="solid")
    document_label = Label(window, text=str(
        medicine[4]), width=window.winfo_screenwidth() // 4, height=(window.winfo_screenheight() // 3) - 6, anchor="n", relief="solid", justify="left")

    name_label.pack()
    expire_date_label.pack()
    document_label.pack()
    window.mainloop()


def rfid_scan(rfid_id: int):
    medicine = get_medicine(rfid_id)
    if not medicine:
        rfid_register(rfid_id)
    else:
        now_exist = 1
        tt = "In"
        if 1 == medicine[5]:
            now_exist = 0
            tt = "Out"
        conn = sqlite3.connect(RESOURCE_DIR_PATH +
                               'medicine.db')
        cur = conn.cursor()
        cur.execute("UPDATE medicine SET now_exist = ? WHERE rfid_id = ?", [now_exist,
                                                                            rfid_id])
        cur.fetchall()
        conn.close()

        window = Tk()
        window.geometry("50x50+" + str(window.winfo_screenwidth() // 2
                                       ) + "+" + str(window.winfo_screenheight() // 2))
        window.resizable(False, False)
        window.title('Medicine InOut')
        Label(window, text=medicine[2] + " is " + tt).pack()
        window.mainloop()
        time.sleep(2)
        window.destroy()


def rfid_register(rfid_id: int):
    window = Tk()
    window.geometry(str(window.winfo_screenwidth() // 4) + "x" +
                    str(window.winfo_screenheight() // 3) + "+0+0")
    window.resizable(False, False)
    window.title('Medicine Register SAK')

    Label(window, text="New Rfid recognized! plz register it now!",
          font=("Purisa", 15)).pack()
    Label(window, text="Name").pack()
    name_entry = Entry(window)
    name_entry.pack()

    expire_date = StringVar(window)

    def choose_date():
        date_window = Tk()

        Label(date_window, text='Choose date').pack(padx=10, pady=10)

        year_text = StringVar(date_window, time.strftime("%Y"))
        month_text = StringVar(date_window, time.strftime("%m"))
        day_text = StringVar(date_window, time.strftime("%d"))

        def choose(time_inf: int):  # 0: year, 1: month, 2: day
            list_window = Tk()
            list_window.geometry("50x50")
            frame = Frame(list_window)
            scrollbar = Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")
            listbox = Listbox(frame, yscrollcommand=scrollbar.set)

            ll = range(int(time.strftime("%Y")),
                       int(time.strftime("%Y")) + 100)
            if time_inf == 1:
                ll = range(1, 12)
            if time_inf == 2:
                mon_day = {"1": 31, "2": 29, "3": 31, "4": 30, "5": 31, "6": 30,
                           "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
                ll = range(1, mon_day[month_text.get()] + 1)
            for l in ll:
                listbox.insert(l, str(l))

            def celected(time_inf: int, num: int):
                snum = str(num + 1)
                if time_inf == 0:
                    year_text.set(str(int(time.strftime("%Y")) + num))
                if time_inf == 1:
                    month_text.set(snum)
                if time_inf == 2:
                    day_text.set(snum)

                list_window.quit()
                list_window.destroy()

            listbox.bind("<<ListboxSelect>>", lambda event: celected(
                time_inf, int(event.widget.curselection()[0])))
            listbox.pack(side="left")
            scrollbar["command"] = listbox.yview
            frame.pack()
            list_window.mainloop()

        for v in [
            ["Year", year_text, 0],
            ["Month", month_text, 1],
                ["Day", day_text, 2]]:
            Button(date_window, text="Choose " + v[0], relief="solid", textvariable=v[1],
                   command=lambda: choose(v[2]), bd=2).pack()

        def done():
            expire_date.set(year_text.get() + "/" +
                            month_text.get() + "/" + day_text.get())
            date_window.quit()
            date_window.destroy()

        Button(date_window, text="Done", command=done).pack()
        date_window.mainloop()

    Button(window, text="Choose Expire Date", command=choose_date).pack()
    Label(window, text="", textvariable=expire_date).pack()

    def master_done():
        register_medicine(name_entry.get(), expire_date.get(), rfid_id)
        window.quit()
        window.destroy()

    Button(window, text="Done", command=master_done).pack()

    window.mainloop()


def start_rfid_scanning():
    reader = RFID()
    running = True

    def end(signal, frame):
        global running
        running = False
        reader.cleanup()

    async def go():
       while True:
            reader.wait_for_tag()
            (err, _) = reader.request()
            if err:
                print(err)
                break
            (err, uid) = reader.anticoll()
            if err:
                print(err)
                break
            id = ""
            for i in uid:
                id += str(i)
            rfid_scan(int(id))
            time.sleep(1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    loop.close()


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
    cur.execute("SELECT id, rfid_id, name, expire_date, document, now_exist FROM medicine WHERE rfid_id = ?", [
                medicine_id])
    rows = cur.fetchall()
    conn.close()
    if len(rows) <= 0:
        return False
    return rows[0]


def get_medicine_by_id(id: int):
    conn = sqlite3.connect(RESOURCE_DIR_PATH +
                           'medicine.db')
    cur = conn.cursor()
    cur.execute("SELECT id, rfid_id, name, expire_date, document, now_exist FROM medicine WHERE id = ?", [
                id])
    rows = cur.fetchall()
    conn.close()
    if len(rows) <= 0:
        return False
    return rows[0]


def register_medicine(name: str, expire_date: str, rfid_id: int):
    conn = sqlite3.connect(RESOURCE_DIR_PATH +
                           'medicine.db')  # get medicine data
    cur = conn.cursor()
    cur.execute("INSERT INTO medicine(rfid_id, name, expire_date) VALUES (?, ?, ?)", [
                rfid_id, name, expire_date])
    conn.commit()
    conn.close()


expire_ids = []


def check_expire_date():  # TODO
    global expire_ids
    expire_ids = []
    window = Tk()
    window.geometry(str(window.winfo_screenwidth() // 5) + "x" +
                    str(window.winfo_screenheight() // 5) + "+0+0")
    window.title('Medicine Expired list - SAK')
    window.resizable(False, False)
    expired_list = Listbox(
        window, selectmode='extended', width=window.winfo_screenwidth() // 5, height=window.winfo_screenheight() // 5, yscrollcommand=True) 
    i = 0
    for medicine in get_medicines():
        times = medicine[3].split("/")
        times = time.mktime(datetime.date(
            times[0], times[1], times[2]).timetuple())
        if int(time.time()) >= times:
            expire_ids.insert(i, medicine[0])
            expired_list.insert(
                i, "Name : " + medicine[2] + ", Expire Date : " + medicine[3])
            i += 1

    if i >= 1:
        expired_list.bind("<<ListboxSelect>>", lambda event: start_info_gui(expire_ids[
            int(event.widget.curselection()[0])]))
        expired_list.pack()
        window.mainloop()
