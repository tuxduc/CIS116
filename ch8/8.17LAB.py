'''
10 -7 4 -39 -6 12 -2

get integers from input
split too create list A
loop while x <0:
    add to a list B (will give us all negative values)

print(sort(list B))
'''
userInput= input()

listA = userInput.split()
listIntegers = []
listforSort= []
for x in listA:
    listIntegers.append(int(x))

for x in listIntegers:
    if x < 0:
        listforSort.append(x)
    else:
        continue

listforSort.sort()
listforSort.reverse()

for x in listforSort:
    print(x,end= ' ')



