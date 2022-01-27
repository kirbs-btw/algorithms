import math

class vector3:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

def sumVector3(vector):
    vectorSum = math.sqrt(vector.x1 ** 2 + vector.x2 ** 2 + vector.x3 ** 2)
    return vectorSum

def calcVector3(vectorA, vectorB):
    """

    :param vectorA: vector A
    :param vectorB: vector B
    :return:
    """

    c1 = vectorB.x1 - vectorA.x1
    c2 = vectorB.x2 - vectorA.x2
    c3 = vectorB.x3 - vectorA.x3

    vectorC = vector3(c1, c2, c3)

    print([vectorC.x1, vectorC.x2, vectorC.x3])

    return vectorC

def addVector3(vectorA, vectorB):
    """
    Add two vectors
    a1 + b1
    a2 + b2
    a3 + b3

    :param vectorA: vektor A
    :param vectorB: vektor B
    :return:
    """

    c1 = vectorB.x1 + vectorA.x1
    c2 = vectorB.x2 + vectorA.x2
    c3 = vectorB.x3 + vectorA.x3

    vectorC = vector3(c1, c2, c3)

    print([vectorC.x1, vectorC.x2, vectorC.x3])
    return vectorC

def main():
    #len vector calc
    vectorA = vector3(1, 4, 5)
    print(sumVector3(vectorA))

    #calc vektor between two
    vectorA = vector3(1, 0, 3)
    vectorB = vector3(-10, 4, 2)
    calcVector3(vectorA, vectorB)

    #add two vektors
    addVector3(vectorA, vectorB)
    pass

if __name__ == '__main__':
    main()
