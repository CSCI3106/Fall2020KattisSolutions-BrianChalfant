# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from math import gcd

p, q, s = map(int, input().split())
if p * q / gcd(p, q) <= s:
    print('yes')
else:
    print('no')