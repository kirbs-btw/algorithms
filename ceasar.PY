
def encriptCeasar(word, num):
    """

    :param word: string
    :param num:  the number it is shifted by !> 27
    :return:
    """

    letters = "abcdefghijklmnopqrstuvwxyz "
    newWord = ""
    for i in word:
        index = -1
        for f in letters:
            index += 1
            if f == i:
                break
        if (index + num) > (len(letters) - 1):
            index = index - len(letters)

        newWord = newWord + str(letters[index + num])


    return newWord

if __name__ == '__main__':
    print(f">{encriptCeasar('abcdefghijk lmno pqrst uvwxyz', 1)}<")