


def main():

    list1 = [
        [1, "hello1", "hello2"],
        [2, "lol", "hi"],
        [3, "more stuff", "even more"]
    ]

    list2 = [1, "hello3", "hello4"]

    key = 1
    savelist = []

    for i in list1:
        if i[0] == key:
            savelist = i

    list2.remove(key)
    savelist.remove(key)

    list2 = savelist + list2
    print(list2)
if __name__ == '__main__':
    main()