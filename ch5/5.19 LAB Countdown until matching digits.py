userInt = int(input())
intToStr = str(userInt)

if 11 > userInt or userInt > 99:
    print('Input must be 11-99')
else:
    print(userInt)
while (userInt % 11 != 0) and 11 <= userInt <= 99:
    userInt -= 1
    print(userInt)
else:
    exit

'''
take the integer

check and seee if the digits are the same
    if the digits are same:
        break
    other wise if the digits are different;
        add 1 to integer
        print integer
'''