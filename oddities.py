# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
outputString = ""
for i in range(n):
    tc = int(input())
    outputString += str(tc) + " is even\n" if tc % 2 == 0 else str(tc) + " is odd\n"
print(outputString)