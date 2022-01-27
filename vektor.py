import math

class vektor3:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

def sumVektor3(vektor):
    vektorSum = math.sqrt(vektor.x1 ** 2 + vektor.x2 ** 2 + vektor.x3 ** 2)
    return vektorSum

def calcVector3(vektorA, vektorB):
    c1 = vektorB.x1 - vektorA.x1
    c2 = vektorB.x2 - vektorA.x2
    c3 = vektorB.x3 - vektorA.x3

    vektorC = vektor3(c1, c2, c3)

    print(vektorC.x1)
    print(vektorC.x2)
    print(vektorC.x3)

    return vektorC

def addVector3(vektorA, vektorB):
    c1 = vektorB.x1 + vektorA.x1
    c2 = vektorB.x2 + vektorA.x2
    c3 = vektorB.x3 + vektorA.x3

    vektorC = vektor3(c1, c2, c3)

    print([vektorC.x1, vektorC.x2, vektorC.x3])

def main():
    #len vektor calc
    vektorA = vektor3(1, 4, 5)
    print(sumVektor3(vektorA))

    #calc vektor between two
    vektorA = vektor3(1, 0, 3)
    vektorB = vektor3(-10, 4, 2)
    #calcVector3(vektorA, vektorB)

    addVector3(vektorA, vektorB)
    pass

if __name__ == '__main__':
    main()
