# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from math import sqrt
cx, cy, n = map(int, input().split())
listening_posts = []
for _ in range(n):
    x, y, r = map(int, input().split())
    distance = sqrt((x - cx)**2 + (y-cy)**2) - r
    listening_posts.append(int(distance))
    # d=√((x_2-x_1)²+(y_2-y_1)²)  Distance Formula
listening_posts.sort()
print(max(0,listening_posts[2]))