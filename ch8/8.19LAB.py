inputValues= input().split()
inputBounds= input().split()

#convert to integers
listValues= []
for x in inputValues:
    listValues.append(int(x))
listBounds= []
for x in inputBounds:
    listBounds.append(int(x))

# print values in range
for x in listValues:
    if listBounds[0]<=x<=listBounds[1]:
        print(x, end=',')
    else:
        continue