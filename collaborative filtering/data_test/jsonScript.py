import json

"""
your py file cannot be named json.py :)

you get a double error and nothing works
"""

def insertData():
    data = {
        "data": [
            [2, 'NULL', 5, 2, 4, 0, 1],
            [1, 1, 3, 2, 4, 5, 'NULL'],
            [0, 0, 2, 2, 5, 4, 0],
            [4, 2, 3, 4, 5, 'NULL', 5],
            [3, 4, 5, 'NULL', 4, 'NULL', 2],
            [3, 3, 'NULL', 'NULL', 4, 3, 2],
            [1, 1, 'NULL', 1, 1, 2, 'NULL'],
        ],
    }

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


def createJson():
    f = open("data.json", "w+")

def getJsonData():

    with open('data.json') as file:
        data = json.load(file)
        print(data)

def main():
    with open('data.json') as file:
        dataSet = json.load(file)
        print(dataSet)


if __name__ == '__main__':
    insertData()
    main()