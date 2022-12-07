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
    for a, f in enumerate(data.matrix):
        for b, l in enumerate(f):
            data.matrix[a][b] = lookupTable.lookupTable[l]

    print(data.matrix)

def shiftData(data):
    result = []
    for row in data.matrix:
        arr = []
        shift = 1
        for i in range(len(row)):
            arr.append(row[i - shift])
        result.append(arr)

    print(result)

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

    print(result)


    pass

text = "hello sir ballzz"
dataObj = data()
dataObj.convertToData(text)
print(dataObj.matrix)
aes(dataObj)