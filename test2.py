def number_of_pennies(d,p=0):
    dollTOpen = d / 100
    total_pennies = dollTOpen + p
    return total_pennies

a = int(input())
b = int(input())
c = int(input())

number_of_pennies(a,b)
number_of_pennies(c)

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only

'''
def mph_and_minutes_to_miles(x,y):
    hours_traveled = minutes_traveled / 60.0
    miles_traveled = hours_traveled * miles_per_hour

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')


            #start of txt repository
def get_minutes_as_hours(orig_minutes):
    minutes = orig_minutes/60
    return minutes

minutes = float(input())
print(get_minutes_as_hours(minutes))


#Read in first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

#Read in second equation, dx + ey = f 
d = int(input())
e = int(input())
f = int(input())

check = False

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if a * x + b * y == c and d * x + e * y == f:
            check = True
            print(f'x = {x} , y = {y}')

if check == False:
    print('There is no solution')

# a * x + b * y = c
# d * x + e * y = f
        
            #end of text reopsitory
'''