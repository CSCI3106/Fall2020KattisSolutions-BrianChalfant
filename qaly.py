# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
tc = int(input())
av = 0.0
for _ in range(tc):
    x, y = map(float, input().split())
    av += x * y
print(av)