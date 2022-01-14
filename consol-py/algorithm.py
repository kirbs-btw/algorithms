import random
import os
import time


def twoLayerList(num):
    arr = list()
    for i in range(num):
        f = list()
        for i in range(num):
            f.append("O")
        arr.append(f)
    return arr

def checkBorder(cord, arr):
    if cord > len(arr) - 1:
        cord = 0
    elif cord == -1:
        cord = len(arr) - 1
    return cord

def randomInput():
    options = [
    "w",
    "a",
    "s",
    "d"
    ]

    comInput = options[random.randint(0,3)]

    return comInput

def moveAroundMultiList(arr):
    start = time.time()
    clear = lambda: os.system('cls')
    x = 0
    y = 0
    i = "go"
    goalx = random.randint(0, len(arr)-1)
    goaly = random.randint(0, len(arr)-1)
    arr[goalx][goaly] = "\033[92mW\033[0m"

    while i != "stop":
        arr[y][x] = "O"
        #i = input("w a s d:")
        i = randomInput()
        if i == "w":
            y -= 1
            y = checkBorder(y, arr)
        elif i == "s":
            y += 1
            y = checkBorder(y, arr)
        elif i == "a":
            x -= 1
            x = checkBorder(x, arr)
        elif i == "d":
            x += 1
            x = checkBorder(x, arr)
        else:
            print("no valid input! (stop, w, a, s, d)")
        arr[y][x] = "\033[91mX\033[0m"


        clear()

        print('Download System Sort\nat kw-corp.de \n')
        for f in arr:
            line = ""
            for j in f:
                line = line + f' {j}'
            print(line)
        print(f'{goaly}/{goalx}, {x}/{y}')
        if goaly == x and goalx == y:
            print("you win!")
            print(round((time.time() - start), 3))
            i = "stop"

def start(n):
    moveAroundMultiList(twoLayerList(n))

if __name__ == '__main__':
    start(10)
