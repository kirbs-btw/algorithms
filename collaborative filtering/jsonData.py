import sqlite3

def inputData():
    data = [
        [2, None, 5, 2, 4, 0, 1],
        [1, 1, 3, 2, 4, 5, None],
        [0, 0, 2, 2, 5, 4, 0],
        [4, 2, 3, 4, 5, None, 5],
        [3, 4, 5, None, 4, None, 2],
        [3, 3, None, None, 4, 3, 2],
        [1, 1, None, 1, 1, 2, None],
    ]

    conn = sqlite3.connect("data.sql")
    cur = conn.cursor()

    for dataLine in data:
        cur.execute()

def defineTable():
    conn = sqlite3.connect("data.sql")
    cur = conn.cursor()

    cur.execute("CREATE TABLE data(a int, b int, c int, d int, e int, f int, g int)")
    conn.commit()

def createSQL():
    f = open("data.sql", "w+")

if __name__ == '__main__':
    inputData()