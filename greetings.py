# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
word = list(input().strip())
for i in range(len(word)):
    if word[i] == 'e':
        word[i] = 'ee'

print("".join(word))