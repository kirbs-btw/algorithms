def getData():
    dataSet = [
        [3, 4, 5, None, 4, 3, 2],
        [3, 3, None, None, 4, 3, 2],
        [1, 1, None, 1, 1, 2, None]
    ]

    return dataSet

def getDiff(dataSet):
    diffSet = []

    userData = dataSet[0]
    workSet = dataSet
    workSet.remove(userData)

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
        avgSet.append(sum / (count**2))
    return avgSet



def main():
    """
    this is the raw design of the algorithm
    it's not scalable jet.
    :return:
    """

    diff = getDiff(getData())
    avgDiff = getAvgDiff(diff)
    
    print(diff)
    print(avgDiff)

if __name__ == '__main__':
    main()