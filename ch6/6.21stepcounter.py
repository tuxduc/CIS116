# Define your function here 
def feet_to_steps(floatPram):
    stepsWalked = int(floatPram/2.5)
    return stepsWalked

if __name__ == '__main__':
    # Type your code here.
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))