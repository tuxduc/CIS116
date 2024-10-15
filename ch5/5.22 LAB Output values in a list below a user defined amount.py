numlist = []
numQty = numlist[0]

for val in range(numQty):
    numlist.append(int(input))

numThreshold = int(input())

for x in numlist:
    if x <= numThreshold:
        print(x, end=',')