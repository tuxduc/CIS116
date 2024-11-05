samples_list = []
#25 62 24 21
tokens = input().split()
for token in tokens:
    samples_list.append(int(token))
  
print('Original samples:', end=' ')
for samples in samples_list:
    print(samples, end=' ')
print()

''' Your code goes here '''
for pos in range(len(samples_list)):
    if samples_list[pos] < 25:
        print(f'{samples_list[pos]} dropped')
        samples_list.remove(samples_list[pos])
    

print('Filtered samples:', end=' ')
for samples in samples_list:
    print(samples, end=' ')
print()