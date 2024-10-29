userInput = input()
listFrominput = userInput.split()

lastName= listFrominput[-1]
firstName= listFrominput[0]
firstInitial = firstName[0]

if len(listFrominput) > 2:
    middleName= listFrominput[1]
    middileInitial = middleName[0]
    print(f'{lastName}, {firstInitial}.{middileInitial}.')
else:
    print(f'{lastName}, {firstInitial}.')