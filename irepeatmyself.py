# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
def repeats(message):
    for j in range(1, len(message)):
        substring = message[:j]
        constructedString = (substring * (len(message) // len(substring)) + (substring[:len(message) % len(substring)]))
        if constructedString.lower().strip() == message.lower().strip():
            return j
    return len(message)

n = int(input())
for i in range(n):
    print(repeats(input()))