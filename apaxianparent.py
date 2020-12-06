# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
first, last = input().split()
suffix = first[-1]
if suffix == 'e':
    fullName = first + "x" + last
elif suffix in ["a", "i", "o", "u"]:
    fullName = first[0:-1] + "ex" + last
else:
    fullName = first + "ex" + last
if suffix == 'x':
    if first[-2] == 'e':
        fullName = first + last
print(fullName)