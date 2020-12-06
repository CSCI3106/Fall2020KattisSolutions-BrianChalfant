# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = -1
while (True):
    n = int(input())
    if n == 0:
        break
    s = "".join(i.upper() for i in input().split())
    encrypted_string = [None] * len(s)
    i = 0
    starting_character = 0
    for c in range(len(s)):
        encrypted_string[i] = s[c]
        i = (i + n)
        if i >= len(s):
            starting_character += 1
            i = starting_character % len(s)
    print("".join(encrypted_string))