# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
number1 = int(input())
number2 = int(input())

if number1 > 0:
    if number2 > 0:
        print(1)
    else:
        print(4)
else:
    if number2 > 0:
        print(2)
    else:
        print(3)