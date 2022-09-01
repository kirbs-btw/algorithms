def getData():
    dataSet = [
        [3, 4, 5, None, 4, None, 2],
        [3, 3, None, None, 4, 3, 2],
        [1, 1, None, 1, 1, 2, None]
    ]

    return dataSet

def getDiff(userData, workSet):
    diffSet = []



    """
    userData is the data of our user 
    in this example it is the first one
    
    workSet is the rest of the data 
    if not removed we would compare the userData to it self 
    """

    for user in workSet:
        diffArr = []
        for index, item in enumerate(user):
            if userData[index] != None and item != None:
                diffArr.append(userData[index] - item)
            else:
                diffArr.append(None)
        diffSet.append(diffArr)

    return diffSet

def getAvgDiff(diffSet):
    avgSet = []

    for userDiff in diffSet:
        sum = 0
        count = 0
        for item in userDiff:
            if item != None:
                sum += item
                count += 1
        avgSet.append(round(sum / (count**2), 5))
    return avgSet

def predict(workData, avgDiff):
    dataPoint = 5

    sumWData = 0
    sumW = 0
    for index, item in enumerate(avgDiff):
        if workData[index][dataPoint] != None:
            sumW += item
            sumWData += item * workData[index][dataPoint]

    return sumWData/sumW

def main():
    """
    this is the raw design of the algorithm
    it's not scalable jet.
    :return:
    """

    dataSet = getData()

    #
    userData = dataSet[0]
    workSet = dataSet
    workSet.remove(userData)
    #

    diff = getDiff(userData, workSet)
    avgDiff = getAvgDiff(diff)

    print(predict(workSet, avgDiff))
    print(diff)
    print(avgDiff)

if __name__ == '__main__':
    main()