numlist = []
numQty = int(input())

for val in range(numQty):
    val = int(input())
    numlist.append(val)

numThreshold = int(input())

for x in numlist:
    if x <= numThreshold:
        print(x, end=',')

'''
VERY GOOD! :)
'''