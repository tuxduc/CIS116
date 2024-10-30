userInput= input()
Rev_userInput=userInput[::-1]

for x in len(userInput)
    x = userInput.find(userInput[0])

'''
#using lists...
userInput= input()
listFrominput= list(userInput) #now we have a list comprising elemnts in input
RevlistFrominput= listFrominput.reverse()

print(listFrominput)
print(RevlistFrominput)
'''


'''
##this acheived 6/10 point on lab

#get user input
userInput= input()
userInputReversed= userInput[::-1]

#determine if it is a palindrome

if userInput == userInputReversed:
    print(f'palindrome: {userInput}')
else:
    print(f'not a palindrome: {userInput}')
    '''


"""
example:
myStr= 'dr awkward'

print(myStr) #dr awkward
print(myStr[::-1]) #drawkwa rd

for each element in the user input:
    check what position that coresponding elemnt is in the reverse in put
then, if the element position are the same:
    is a palindrome
if any one elemnt has a missmatch:
    not a palindrome


procedure:
1 get user input
2 split that input
3 make new list that is reverse of split (should have same values in each element and position)
4 compare
5 proceed to if statement

Example:
racecar= r,a,c,e,c,a,r OR r,a,c,e,c,a,r

if user word reveresed is same as user word, then:
    word is a palindrome
otherwise:
    not a palindrome
"""