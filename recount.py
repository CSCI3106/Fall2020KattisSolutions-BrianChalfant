# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from collections import Counter
name = input()
candidates = {}
while name != "***":
    if name in candidates.keys():
        candidates[name] += 1
    else:
        candidates[name] = 1
    name = input()

cnt = Counter(candidates)
high = cnt.most_common(2)
if high[0][1] == high[1][1]:
    print("Runoff!")
else:
    print(high[0][0])