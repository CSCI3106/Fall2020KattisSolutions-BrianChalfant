# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
for i in range(n):
    b, p = input().split()
    b = float(b)
    p = float(p)
    calculated = ((60 * b)/p)
    t = (60/p)
    min = calculated - t
    max = calculated + t
    print("{0:.4f} {1:.4f} {2:.4f}".format(min, calculated, max))