userInt = int(input())
intToStr = str(userInt)
#if 11 <= userInt <= 99:

# print(intToStr[0]) we can index the str

#for x in range(len(intToStr)):
while 11 <= userInt <= 99:
    if intToStr[0] == intToStr[1]:
        exit()
    else:
        userInt += 1
        print(userInt)
'''
take the integer

check and seee if the digits are the same
    if the digits are same:
        break
    other wise if the digits are different;
        add 1 to integer
        print integer
'''