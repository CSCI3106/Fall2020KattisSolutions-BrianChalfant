# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
atBat = n
bases = 0
turns = list(map(int, input().split()))
for i in range(n):
    inpt = turns[i]
    if inpt >= 0:
        bases += inpt
    else:
        atBat -= 1
print(float(bases)/float(atBat))