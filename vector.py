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

    print([vC.x1, vC.x2, vC.x3])

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

    print([vC.x1, vC.x2, vC.x3])
    return vC

def main():
    #len vector calc
    vA = vector3(1, 4, 5)
    print(sumVector3(vA))

    #calc vektor between two
    vA = vector3(1, 0, 3)
    vB = vector3(-10, 4, 2)
    calcVector3(vA, vB)

    #add two vektors
    addVector3(vA, vB)

if __name__ == '__main__':
    main()
