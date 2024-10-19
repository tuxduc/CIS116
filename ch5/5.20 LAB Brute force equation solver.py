#Read in first equation, ax + by = c '''
a = 8 #int(input())
b = 7 #int(input())
c = 38 #int(input())

#Read in second equation, dx + ey = f '''
d = 3 #int(input())
e = -5 #int(input())
f = -1 #int(input())

#''' Type your code here. '''
x= 0
y= 0
#eq1 = a*x + b*y == c
#eq2 = d*x + e*y == f

for x in range(-10,10):
    for y in range(-10,10):
        if a*x + b*y == c and d*x + e*y:
         check = True
         print(f'x= {x} , y = {y}')

if check == False:
    print('There is no solution')