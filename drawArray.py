import turtle
import time
import random


def drawArray(arr):
    print(arr)
    t = turtle.Turtle()
    t.pensize(10)
    t.speed(500)

    color = [
        '#59a1d9',
        '#a3d8e6',
        '#1d1d1b',
        '#ea498b'
    ]

    for i in arr:
        t.pensize(random.randint(1, 25))
        t.color(color[random.randint(0, (len(color) - 1))])
        t.penup()
        t.setx(i[0])
        t.sety(i[1])
        t.pendown()
        t.forward(1)

    time.sleep(5)
    pass


def randMultiArr(size):
    arr = []
    for i in range(size):
        randMax = 500
        randMin = -randMax
        subArr = [random.randint(randMin, randMax), random.randint(randMin, randMax)]
        arr.append(subArr)
    return arr


if __name__ == '__main__':
    drawArray(randMultiArr(500))

# download System Sort kw-corp.de
