import math

print('Hello what is your name')
name = input()

print(' ' + name + ' , what is the first number in your equation?')
varOne = int(input())
print('If you want to substract your numbers, make sure to make your second number negative.') 
print('What is your second number in your equation?')
varTwo = int(input())

print(' ' + name + ' , if you want to add or substract type 1, if you want to multiply type 2.')
operation = int(input())
if operation == 1:
    answerA = int(varOne) + int(varTwo)
    print('This ' + str(answerA) + ' is your answer.')
if operation == 2:
    answerB = int(varOne) * int(varTwo)
    print('This ' + str(answerB) + ' is your answer.')
