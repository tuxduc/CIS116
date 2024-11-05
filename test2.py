# Read input and split input into tokens
tokens = input().split()

temperature_samples = []
for token in tokens:
    temperature_samples.append(int(token))

print(f'All data: {temperature_samples}')

''' Your code goes here '''
sum_good= 0
for pos,value in enumerate(temperature_samples):
    if pos%2 != 0 and value<=50:
        print(f'Index{pos}: value is{value}')
        sum_good += value

print(f'Sum of selected elements is: {sum_good}')