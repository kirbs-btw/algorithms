import json

def getData():
    with open('data.json') as file:
        return json.load(file)['data']



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
            try:
                diffArr.append(userData[index] - item)
            except:
                diffArr.append(None)
        diffSet.append(diffArr)

    return diffSet

def getAvgDiff(diffSet):
    avgSet = []

    for userDiff in diffSet:
        sum = 0
        count = 0
        for item in userDiff:
            try:
                sum += item
                count += 1
            except:
                pass
        avgSet.append(round(sum / (count**2), 5))
    return avgSet

def predict(workData, avgDiff):
    dataPoint = 5

    sumWData = 0
    sumW = 0
    for index, item in enumerate(avgDiff):
        try:
            sumW += item
            sumWData += item * workData[index][dataPoint]
        except:
            pass
    return sumWData/sumW

def main():
    """
    this is the raw design of the algorithm
    it's not scalable jet.
    :return:
    """

    dataSet = getData()
    print(dataSet)

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