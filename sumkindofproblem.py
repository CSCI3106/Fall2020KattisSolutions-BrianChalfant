# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
p = int(input())

for i in range(p):
    pos, odd, even = 0, 0, 0
    vars = input().split(sep=" ")
    k = int(vars[0])
    n = int(vars[1])
    for m in range(0, n+1):
        pos += m
    for j in range(0, ((n) * 2)):
        if j%2 > 0:
            odd += j
    for l in range(0, ((n+1) * 2)):
        if l%2 == 0:
            even += l
    print(k, pos, odd, even)