import random
import os
import time


# random list generator
def randList(numItems, start, end):
    """random list generator for testing sorting algorithms"""

    arr = list()
    for i in range(numItems):
        arr.append(random.randint(start, end))

    return arr


# Bubble Sort sorting algorithm ###############################################################
def bubbleSort(list):
    """input a list of numbers a argument"""

    lenList = len(list)
    for i in range(lenList - 1):
        for j in range(0, lenList - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


################################################################


# Moving around in a 2D plane #####################################################
def twoLayerList(num):
    """
    creates 2d plane num = NxN size

    example: n = 3
        [
        [0,0,0]
        [0,0,0]
        [0,0,0]
        ]
    :param n: size of the grid 

    """
    arr = list()
    for i in range(num):
        f = list()
        for i in range(num):
            f.append("O")
        arr.append(f)
    return arr


def checkBorder(cord, arr):
    """
    checks for the end of the plane
    if so focus element switches side

    cord = coordinate at the plane
    arr = plane array

    """

    if cord > len(arr) - 1:
        cord = 0
    elif cord == -1:
        cord = len(arr) - 1
    return cord


def randomInput():
    """
    creates random inputs
    """

    options = [
        "w",
        "a",
        "s",
        "d"
    ]

    comInput = options[random.randint(0, 3)]

    return comInput


def moveAroundMultiList(arr):
    """
    moving algorithm for a 2D plane
    arr needs to be a 2 dimensional array
    """

    start = time.time()
    clear = lambda: os.system('cls')
    x = 0
    y = 0
    i = "go"
    goalx = random.randint(0, len(arr) - 1)
    goaly = random.randint(0, len(arr) - 1)
    arr[goalx][goaly] = "\033[92mW\033[0m"

    while i != "stop":
        arr[y][x] = "O"
        # i = input("w a s d:")
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
            playtime = round((time.time() - start), 3)
            print(playtime)
            f = open("data.txt", "a")
            f.write(f'\n{playtime}')
            f.close()
            i = "stop"


def statistics(fromSize, toSize, count):
    """
    tests the random generator
    fromSize = size of the array where it starts (needs to be >2)
    toSize = max array size

    count = how many iterations it does per size

    :param fromSize: size where it starts the size of the grid needs to be >2
    :param toSize: biggest size of the grid
    :param count: how many times does it test each grid
    """

    for f in range(fromSize, toSize):
        print(f)
        m = open("data.txt", "a")
        m.write(f'\nsize: {f}')
        m.close()
        for i in range(count):
            moveAroundMultiList(twoLayerList(f))


#####################################################

# random password generator #########################

def generatePassword(length):
    """
    generates random password
    argument = length = len passwort

    :param length: describes lenth of the outcome password
    :return: returns randompassword depending on the length argument

    """

    dic = "abcdefghijklmnopqrstuvwxyz1234567890.,+=/!&%$§ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = len(dic)
    pw = ""

    for i in range(length):
        index = random.randint(0, (num - 1))
        pw = pw + dic[index]

    return pw

######################################################

if __name__ == '__main__':
    # print(bubbleSort(randList(50, 0, 50)))
    statistics(2, 25, 100)
    #print(generatePassword(25))

# Bastian Lipka
