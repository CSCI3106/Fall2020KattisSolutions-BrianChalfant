# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020

grandmastring = input()
length = int(len(grandmastring)/3)
first = grandmastring[:length]
second = grandmastring[length: int((length * 2))]
third = grandmastring[int((length * 2)):]

if first == second == third:
    print(first)
elif first == second:
    print(first)
elif second == third:
    print(second)
elif first == third:
    print(first)