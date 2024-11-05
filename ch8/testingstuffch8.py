# Read input and split input into tokens
tokens = input().split()

sequence_data = []
for token in tokens:
    sequence_data.append(int(token))

print(f'Sequence: {sequence_data}')

max_diff = None

''' Your code goes here '''
for i,null in enumerate(sequence_data):
    neighborDiff = sequence_data[i - 1] - sequence_data[i]
    print(f'{sequence_data[i - 1]} - {sequence_data[i]} = {neighborDiff}')
    max_diff = 0
    if neighborDiff > max_diff:
        max_diff += neighborDiff
    else:
        continue
        
print(f'The maximum difference between two neighboring values is {max_diff}')