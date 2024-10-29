# Define your function here.
    ##repurposed code from lab4.19
def days_in_feb(user_year):
    if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
        numDays = 29
    ##if above is true, it is a leap year and will have 29 days

    else:
        numDays = 28
    ##otherwise, is not a leap year and will have 28 days
    return numDays

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    userYear = int(input())

    print(f'{userYear} has {days_in_feb(userYear)} days in February.')