# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
tc = int(input())
sum = 0
for _ in range(tc):
    line = input()
    sum += int(line[0:-1]) ** int(line[-1])
print(sum)