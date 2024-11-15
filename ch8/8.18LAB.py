userInput= input()
userList= userInput.split()
listIntegers = []
#convert to integers
for x in userList:
    listIntegers.append(int(x))

# to get middle value: (len(list)-1/2)+1
#valMiddle= listIntegers[(len(list)-1/2)]
valMiddle= listIntegers[int((len(listIntegers)-1)/2)]

if len(listIntegers)>9:
    print("Too many inputs")
    exit
else:
    print(f"Middle item: {valMiddle}")
