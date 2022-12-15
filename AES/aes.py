import math
import lookupTable

class data:
    def __init__(self):
        self.matrix = []
        self.size = 4

    def addRow(self, new_row):
        self.matrix.append(new_row)

    def convertToData(self, inputData):
        arr = []
        for char in inputData:
            arr.append(char)
            if len(arr) == self.size:
                self.matrix.append(arr)
                arr = []

def aes(data):
    subData(data)
    shiftData(data)
    mixData(data)
    # keyAddData(data)

def subData(data):
    for indexI, i in enumerate(data.matrix):
        for indexJ, j in enumerate(i):
            #
            data.matrix[indexI][indexJ] = chr(ord(j) + 2)

    for i in data.matrix:
        print(i)
    print()

def shiftData(data):
    result = []
    for row in data.matrix:
        arr = []
        shift = 1
        for i in range(len(row)):
            arr.append(row[i - shift])
        result.append(arr)

    for i in result:
        print(i)
    print()

    data.matrix = result

def convertData(data):
    x = data
    for i, row in enumerate(x):
        for j, char in enumerate(row):
            x[i][j] = ord(char)
    return x

def mixData(data):
    x = convertData(data.matrix)

    y = [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [7, 8, 9, 10],
        [11, 12, 13, 14]
    ]

    result = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    data.matrix = result

    convertMatrixToChar(data)

    for i in result:
        print(i)
    print()

def convertMatrixToChar(data):
    for row, i in enumerate(data.matrix):
        for col, j in enumerate(i):
            data.matrix[row][col] = chr(j%256)


text = "hello sir ballzz"
dataObj = data()
dataObj.convertToData(text)

for i in dataObj.matrix:
    print(i)
print()

aes(dataObj)