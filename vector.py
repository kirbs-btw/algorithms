import math

class vector3:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def print(self):
        """
        prints the vector3 because printing
        :return:
        """

        values = [self.x1, self.x2,  self.x3]
        print(values)

def sumVector3(vX):
    vSum = math.sqrt(vX.x1 ** 2 + vX.x2 ** 2 + vX.x3 ** 2)
    return vSum

def calcVector3(vA, vB):
    """

    :param vectorA: vector A
    :param vectorB: vector B
    :return:
    """

    c1 = vB.x1 - vA.x1
    c2 = vB.x2 - vA.x2
    c3 = vB.x3 - vA.x3

    vC = vector3(c1, c2, c3)

    return vC

def addVector3(vA, vB):
    """
    Add two vectors
    a1 + b1
    a2 + b2
    a3 + b3

    :param vA: vektor A
    :param vB: vektor B
    :return:
    """

    c1 = vB.x1 + vA.x1
    c2 = vB.x2 + vA.x2
    c3 = vB.x3 + vA.x3

    vC = vector3(c1, c2, c3)

    return vC

def dotProduct(vA, vB):
    """
    calculates the scalar product of two vector3´s
    a1 * b1 + a2 * b2 + a3 * b3

    :param vA:
    :param vB:
    :return:
    """

    dotP = (vA.x1 * vB.x1) + (vA.x2 * vB.x2) + (vA.x3 * vB.x3)
    return dotP

def crossProduct(vA, vB):
    c1 = vA.x2 * vB.x3 - vA.x3 * vB.x2
    c2 = vA.x3 * vB.x1 - vA.x1 * vB.x3
    c3 = vA.x1 * vB.x2 - vA.x2 * vB.x1

    vC = vector3(c1, c2, c3)

    return vC

def main():
    #len vector calc
    vA = vector3(1, 5, 7)
    vB = vector3(5, -1, 2)

    vA.print()

    print(sumVector3(vA))

    print(dotProduct(vA, vB))

    #calc vektor between two
    calcVector3(vA, vB).print()

    #add two vektors
    addVector3(vA, vB).print()

    crossProduct(vA, vB).print()

if __name__ == '__main__':
    main()
