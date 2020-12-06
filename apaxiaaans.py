# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = input()
i = n[0]
letters = [l for l in n]
letters.append(".")
newarray = []
for i in range((len(letters) -1)):
    if letters[i] == letters[i+1]:
        pass
    else:
        newarray.append(letters[i])

print("".join(newarray))
