import sqlite3
import random

def main():
    f = open("db.sql", "w+")

    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "CREATE TABLE test(column varchar(10), column2 varchar(10), column3 varchar(10), column4 varchar(10))"
    cur.execute(command)
    conn.commit()
    conn.close()

def createData():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    for i in range(100):
        command = f"INSERT INTO test VALUES({random.randint(0, 100)}, {random.randint(0, 100)}, {random.randint(0, 100)}, {random.randint(0, 100)})"
        cur.execute(command)
        print(command)
        conn.commit()

if __name__ == '__main__':
    createData()