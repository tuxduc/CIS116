import math

list =[]
# Define your function here.
def max_magnitude(int1,int2,int3):
    list.append(int1)
    list.append(int2)
    list.append(int3)
    largest = 0
    for i in list:
        if abs(i)>largest:
            largest = i

    return largest

if __name__ == '__main__':
    # Type your code here.
    print(max_magnitude(int(input()),int(input()),int(input())))

'''
brainstorming:
can put ints into a list and get the absolute value of them, then get max value
'''