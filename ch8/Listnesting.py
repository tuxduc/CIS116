myList = ['apple', 'tiger', 'bear']

#for x in myList:
#    print(x)


myListComplex = [
    ['apple','red','round'],
    ['tiger','orange','striped'],
    ['bear','large','furry']
]

for row in myListComplex:
    for x in row:
        print(x, end=" ")
    print()