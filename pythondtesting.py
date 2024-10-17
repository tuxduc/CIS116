userInt = int(input())
intToStr = str(userInt)

#print(intToStr[0])
#print(intToStr[1])
    
while (userInt % 11 != 0) and 11 <= userInt <= 99:
    userInt -= 1
    print(userInt)
else:
    print('They are the same now!')
    print('Goodbye')
    exit

'''
first_value = int(input())
last_value = int(input())
sum_vals = 0

for x range(first_value, last_value + 1):
    sum_vals += 1
    print(x)

print(f'Sequence sum: {sum_vals}')
'''