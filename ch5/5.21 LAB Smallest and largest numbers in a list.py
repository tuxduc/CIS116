#numList =[int(input()), int(input()), int(input()), int(input()), int(input()), int(input())]
numList = []
max= 0
min = 100

#for x numList:
#   if x > max:
#       max = x
#   if x < min
#       min = x
# print(f'{min} and {max}')
userinput = int(input())

while userinput != 0:
        numList.append(userinput)
else:
    break


for x in numList:
   if x > max:
       max = x
   if x < min and x > 0:
        min = x
print(f'{min} and {max}')    