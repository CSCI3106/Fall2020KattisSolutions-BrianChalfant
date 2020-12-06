# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import math

n = int(input())
p = []
for i in range(1, int(math.sqrt(n)+2)):
    if n % i == 0:
        p.append(i)
        p.append(int(n/i))
p = list(set(p))
p.sort()
print(" ".join(str(i-1) for i in p))