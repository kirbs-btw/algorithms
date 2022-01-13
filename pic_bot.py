count = 3 -1
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

list = ["w", "i", "t", "u"]

countFar = True

while countFar:
    if num6 > count:
        num6 = 0
        num5 = num5 + 1
        if num5 > count:
            num5 = 0
            num4 = num4 + 1
            if num4 > count:
                num4 = 0
                num3 = num3 + 1
                if num3 > count:
                    num3 = 0
                    num2 = num2 + 1
                    if num2 > count:
                        num2 = 0
                        num1 = num1 + 1
                        if num1 > count:
                            countFar = False
                        else:
                            num6 = num6 + 1
                    else:
                        num6 = num6 + 1
                else:
                    num6 = num6 + 1
            else:
                num6 = num6 + 1
        else:
            num6 = num6 + 1
    else:
        num6 = num6 + 1

    #print(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6))
    print(list[num1] + list[num2] + list[num3] + list[num4] + list[num5] + list[num6])
