# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
print(int(("0b" + str(bin(n))[-1:1:-1]), 2))