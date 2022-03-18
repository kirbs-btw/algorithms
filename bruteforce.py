
def run():
    for i in range(0, 99999999999999):
        #print(i)
        main(i)

def findExponent(num, len):
    exponent = 0
    run = True

    while run:
        calc = num / (len ** exponent)
        if calc > 1:
            exponent += 1
        else:
            run = False
    exponent -= 1
    if exponent < 0:
        exponent = 0
    return exponent

def main(num):
	"""
	char = the set of characters that are used add some to get more 
	
	"""
    char = "abcdefghijklmnopqrstuvwxyz"
    highestExponent = findExponent(num, len(char))
    exponent = highestExponent
    text = ""
    while exponent > -1:
        count = num // len(char) ** exponent
        num = num - (len(char) ** exponent * count)
        text += char[count-1]
        exponent -= 1
    print(text)

def test():
    print(5**0)

if __name__ == '__main__':
    run()