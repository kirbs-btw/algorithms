import turtle
import time
import random

def star(size, speed):
    """
    little play around with turtle
    random start with random colors

    :param size: number of lines
    :param speed: speed of the turtle
    :return: none - window of the turtle
    """

    color = [
        '#59a1d9',
        '#a3d8e6',
        '#1d1d1b',
        '#ea498b'
    ]

    bob = turtle.Turtle()

    bob.speed(speed)
    bob.pensize(5)
    for i in range(size):
        bob.color(color[random.randint(0, (len(color) - 1))])
        walk = random.randint(0, 250)
        bob.forward(walk)
        bob.backward(walk)
        bob.left(random.randint(0, 90))

    time.sleep(5)

if __name__ == '__main__':
    star(500, 50)

#kw-corp.de - download System Sort
#Bastian Lipka