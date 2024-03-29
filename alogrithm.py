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
# random word list generator ######################
def randomBrutForceDic():
    """

    :return: list of random strings containing the characters in the list
    """
    arr = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]

    wordList = list()

    lenString = 15

    for i in range(70):
        word = ""
        for j in range(lenString):
            word = word + arr[random.randint(0, len(arr) - 1)]
        wordList.append(word)
    return wordList
#################################################################

# binary converter ##############################################

def convertFromBinary(f):
    """
    :param f:binary input
    :return: returns real number

    """

    count = 0
    j = len(str(f))

    for i in str(f):
        j -= 1
        if i == "0":
            pass
        elif i == "1":
            add = 2 ** j
            count = count + add

    return count


def convertToBinary(num):
    """
    :param num: integer
    :return: returns binary number as string
    """

    binaryOut = ""

    # find highest exponent
    highestExpo = 0
    j = 0
    run = True
    while run:
        if 2 ** j < num:
            j += 1
        elif 2 ** j > num:
            highestExpo = j - 1
            run = False
        elif 2 ** j == num:
            highestExpo = j
            run = False
    ################

    num = num - 2 ** highestExpo
    binaryOut = binaryOut + "1"
    rangeInt = highestExpo

    for i in range(rangeInt - 1):
        highestExpo -= 1
        if 2 ** highestExpo > num:
            binaryOut = binaryOut + "0"
        elif 2 ** highestExpo <= num:
            binaryOut = binaryOut + "1"
            num = num - 2 ** highestExpo

    return binaryOut

#################################################################

# executes simple quadratic function ########################
def quadraticFuntion(inputstr, min, max, step):
    """
    understands x*n+f
    exp. x*5-1
    :param step: step value
    :param max: end value
    :param min: start value
    :param inputstr:
    :return: returns array of nubers in range min to max in steps
    """
    #gets constant value
    constant = ""
    go = False
    for i in inputstr:
        if i == "+" or i == "-":
            constant += i
            go = True
        elif go:
            constant += i

    #gets n value
    n = ""
    go = False
    for i in inputstr:
        if i == "*":
            go = True
        elif i == "+" or i == "-":
            go = False
        elif go:
            n += i

    values = list()

    #does the function for values

    while min <= max + step:
        value = min * float(n) + float(constant)
        values.append(round(value, 5))
        min += step

    return values
###########################################################


if __name__ == '__main__':
    # print(bubbleSort(randList(50, 0, 50)))
    statistics(2, 25, 100)
    # print(generatePassword(25))
    # print(randomBrutForceDic())
    # print(convertFromBinary("10101110011"))
    # print(convertToBinary(1535))

# Bastian Lipka
