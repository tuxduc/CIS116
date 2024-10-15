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

while userTxt not ('Done' or 'done' or 'd'):

    userTxt = input() [::-1]
    print(userTxt)
    continue
else:
    exit
