import sqlite3

"""
i use sql as temp method 
i think about using json but i'm still learning on how to use it :)
"""


def inputData():
    data = [
        [2, 'NULL', 5, 2, 4, 0, 1],
        [1, 1, 3, 2, 4, 5, 'NULL'],
        [0, 0, 2, 2, 5, 4, 0],
        [4, 2, 3, 4, 5, 'NULL', 5],
        [3, 4, 5, 'NULL', 4, 'NULL', 2],
        [3, 3, 'NULL', 'NULL', 4, 3, 2],
        [1, 1, 'NULL', 1, 1, 2, 'NULL'],
    ]

    conn = sqlite3.connect("data.sql")
    cur = conn.cursor()

    for dataLine in data:
        cur.execute(f"INSERT INTO data VALUES({dataLine[0]},{dataLine[1]},{dataLine[2]},{dataLine[3]},{dataLine[4]},{dataLine[5]},{dataLine[6]})")
    conn.commit()

def checkSQL():
    conn = sqlite3.connect("data.sql")
    cur = conn.cursor()

    data = cur.execute("SELECT * FROM data").fetchall()
    for i in data:
        print(i)

def defineTable():
    conn = sqlite3.connect("data.sql")
    cur = conn.cursor()

    cur.execute("CREATE TABLE data(a int, b int, c int, d int, e int, f int, g int)")
    conn.commit()

def createSQL():
    f = open("data.sql", "w+")

if __name__ == '__main__':
    checkSQL()