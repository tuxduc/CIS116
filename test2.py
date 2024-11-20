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

print(f'Sum of selected elements is: {sum_good}')a

def word_frequencies():
    
    words = input("Enter a list of words: ").split()
    
    frequency = {}
    
    for word in words:
        word_lower = word.lower() 
        if word_lower in frequency:
            frequency[word_lower] += 1
        else:
            frequency[word_lower] = 1
    
    for word in words:
        print(f"{word} {frequency[word.lower()]}")
        
word_frequencies()