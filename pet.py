# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
contestants = []
max = 0
for i in range(0, 5):
    sum = 0
    numberString = input().split()
    for j in numberString:
        sum += int(j)
    contestants.append(sum)
    if sum > contestants[max]:
       max = i
print(max + 1, contestants[max])