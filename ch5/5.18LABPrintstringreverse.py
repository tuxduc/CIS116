'''
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
'''
userTxt = input()
exitTxt = ['Done', 'done', 'd']

while userTxt not in exitTxt:
    print(userTxt[::-1])
    userTxt = input()
    continue
else:
    print('Goodbye!')
    exit

'''
atmpt 1:
if userTxt in exitTxt:
    print('goodbye!')
    exit
else:
    print(userTxt)
    continue
'''