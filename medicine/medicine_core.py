import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import sak_core


def start():
    conn = sqlite3.connect(sak_core.RESOURCE_DIR_PATH + 'medicine.db')  # get medicine data
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
