import sqlite3
import tkinter as tk

def getData(dbName):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = f"SELECT * FROM {dbName}"

    data = cur.execute(command).fetchall()

    conn.close()
    return data


