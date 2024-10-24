# Define your function here
def jiffies_to_seconds(user_jiffies):
    numSeconds = user_jiffies/100
    return numSeconds

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    numJiffies = float(input())
    print(f'{jiffies_to_seconds(numJiffies):.3f}') 