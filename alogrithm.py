import random

def bubbleSort(list):
    """input a list of numbers a argument"""

    lenList = len(list)
    for i in range(lenList -1):
        for j in range(0, lenList-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

#more algorithms comming <3

def randList(numItems, start, end):
    arr = list()
    for i in range(numItems):
        arr.append(random.randint(start, end))

    return arr

if __name__ == '__main__':
    print(bubbleSort(randList(50, 0, 50)))

#Bastian Lipka
