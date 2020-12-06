# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
outputString = ""
for i in range(n):
    r, e, c = score = map(int, input().split())
    if r > e - c:
        outputString += "do not advertise\n"
    elif r == (e - c):
        outputString += "does not matter\n"
    else:
        outputString += "advertise\n"
print(outputString)