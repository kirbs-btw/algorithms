
def readData():
    data = open("data.txt", "r+").readlines()
    averageList = []
    count = 0
    sum = 0
    for i in data:
        count += 1
        i = i[0:-1]
        print([i])
        if "size" in i or i == []:
            count -= 1
            sum = sum / count
            averageList.append(round(sum, 5))
            count = 0
            sum = 0
        else:
            sum += float(i)

    print(averageList)
readData()