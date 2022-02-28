import sqlite3

def initSQL():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "CREATE TABLE prime(number INT)"
    cur.execute(command)
    conn.commit()

def save(n):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = f"INSERT INTO prime VALUES({n})"
    cur.execute(command)
    conn.commit()
    pass

def printTable():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "SELECT * FROM prime"
    table = cur.execute(command).fetchall()

    for i in table:
        print(i[0])

def tableDel():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "DELETE FROM prime"
    cur.execute(command)
    conn.commit()
    print("DONE")

def main(n):
    """
    slow way to find prime nums
    :param n:
    :return:
    """
    lastNums = []
    primeNums = []
    for j in range(10000000):
        isPrime = True
        for i in lastNums:
            if n % i == 0:
                isPrime = False
        if isPrime:
            save(n)
            print(n)
        lastNums.append(n)
        n += 1


if __name__ == '__main__':
    # printTable()
    main(2)
    # tableDel()