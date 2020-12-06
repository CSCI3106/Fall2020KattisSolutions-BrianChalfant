# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
number_of_blocks = int(input())
blocks = list(map(int, input().split()))
value = blocks[0]
towers = 1
for i in range(len(blocks)):
    if blocks[i] > value:
        towers += 1
        value = blocks[i]
    else:
        value = blocks[i]

print(towers)