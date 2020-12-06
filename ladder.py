# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from math import radians, sin, ceil
h, v = input().split()
h = int(h)
v = int(v)
print(ceil(h/sin(radians(v))))