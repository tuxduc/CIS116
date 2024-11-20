userInput= input()

numsList= userInput.split()
    #print(numsList)
floatsList= [float(x) for x in numsList]
    #print(floatsList)
    #print(floatsList[0] + floatsList[1])
print(f'{max(floatsList):.2f} {sum(floatsList)/len(floatsList):.2f}')

# test set(float): 3.5 4.9 11.3 -5.11
#test set(int): 1 2 3 4 5