import json

def main():
    data = {
        "a":4,
        "b": 1,
        "c":43,
        "d":7
        }

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    with open('data.json') as file:
        dataSet = json.load(file)
        print(dataSet)


if __name__ == '__main__':
    main()