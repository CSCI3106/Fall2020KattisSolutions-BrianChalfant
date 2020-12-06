# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
line = [i for i in input()]
newline = []
buffer = 0
for i in range(len(line)-1,-1, -1):
    if line[i] == '<':
        buffer += 1
    else:
        if buffer > 0:
            buffer -= 1
        else:
            newline.append(line[i])
print("".join(newline[::-1]))