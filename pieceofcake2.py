# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n, h, v = input().split()
n = int(n)
h = int(h)
v = int(v)
midpoint = n/2
if h < midpoint:
    h = n - h
if v < midpoint:
    v = n - v
print(h * v * 4)