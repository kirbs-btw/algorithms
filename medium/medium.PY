import numpy as np

def main():
    arr = np.random.rand(100)
    count = 0

    for i in arr:
        count += i

    med = count / len(arr)
    print(med)

if __name__ == '__main__':
    main()
