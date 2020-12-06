# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020

import math

def find_dist(x, y):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))


keypad = []


def find_coords(num):
    for i in keypad:
        if num in i:
            return keypad.index(i), i.index(num)

for _ in range(3):
    keypad.append(list(input().split()))
a = find_coords("1")
dist = 0.0
for i in range(2, 10):
    b = find_coords(str(i))
    dist += find_dist(a, b)
    a = b

print("{:.11}".format(dist))