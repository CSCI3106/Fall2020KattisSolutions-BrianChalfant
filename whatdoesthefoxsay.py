# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
for _ in range(n):
    fullMessage = input().split()
    end = False
    knownAnimals = []
    while end != True:
        x = input()
        if x == "what does the fox say?":
            end = True
        else:
            x = x.split()
            knownAnimals.append(x[2])
    print(" ".join([x for x in fullMessage if x not in knownAnimals]))