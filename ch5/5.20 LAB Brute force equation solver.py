#Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

#Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

#''' Type your code here. '''
x= 0
y= 0
#eq1 = a*x + b*y == c
#eq2 = d*x + e*y == f

check = False

for x in range(-10,10,1):
    for y in range(-10,10,1):
        if a*x + b*y == c and d*x + e*y == f:
         check = True
         print(f'x = {x} , y = {y}')

if check == False:
    print('There is no solution')