
def readData():
    """
    reads the data file of the random grid algorithm

    :return:
    """
    data = open("data.txt", "r+").readlines()
    averageList = []
    count = 0
    sum = 0
    for i in data:
        count += 1
        i = i[0:-1]
        if "size" in i or i == []:
            count -= 1
            try:
                sum = sum / count
            except:
                pass
            averageList.append(round(sum, 5))
            count = 0
            sum = 0
        else:
            sum += float(i)

    print(averageList)
    

    #prints averageList in cut up chuncks to use it further in excel

    for f in averageList:
        m = ""
        for l in str(f):
            if l == ".":
                l = ","
            m = m + l
        print(m)

    return averageList
readData()