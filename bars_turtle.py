import turtle
import time
import random

def printBars(values, width):
    doGrid()
    t = turtle.Turtle()
    t.penup()
    t.backward(200)
    t.pendown()
    t.speed(0)
    for i in values:
        printBar(i ,t, width)
    time.sleep(5)

def randomColor():
    color = f"#{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    return color

def randomValues(count, a, b):
    arr = []
    for i in range(count):
        arr.append(random.randint(a, b))

    return arr

def printBar(value, t, width):
    t.color(randomColor())
    t.penup()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.pendown()
    t.forward(value)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(value)
    t.end_fill()
    t.left(90)

def doGrid():
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t2.speed(0)
    t3.speed(0)

    # t2
    t2.penup()
    t2.backward(200)
    t2.pendown()
    t2.forward(700)

    # t3
    t3.penup()
    t3.backward(200)
    t3.left(90)
    t3.pendown()
    t3.forward(500)

if __name__ == '__main__':
    printBars(randomValues(10, 0, 250), 25)

