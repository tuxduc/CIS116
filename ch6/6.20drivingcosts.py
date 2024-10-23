# Define your function here.

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    cost = miles_driven/miles_per_gallon * dollars_per_gallon
    return cost## returns dollar cost to drive those miles

if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=10):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=50):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=400):.2f}')
    
