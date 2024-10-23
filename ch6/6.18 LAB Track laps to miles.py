# Define your function here 

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
def laps_to_miles(num_laps):
    miles = num_laps * .25 
    return miles

print(f'{laps_to_miles(float(input())):.2f}')