import json

class jsonData:
    def __init__(self):
        self.path = 'data.json'

    def insertData(self, dataSet):
        with open(self.path, 'w') as file:
            json.dump(dataSet, file)

    def getData(self):
        with open(self.path) as file:
            return json.load(file)

def main():
    data = jsonData()
    print(data.getData())

if __name__ == '__main__':
    main()