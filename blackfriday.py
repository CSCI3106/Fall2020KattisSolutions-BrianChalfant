# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
results = list(map(int, input().split()))
invalids = []
addresses = {}
for i in range(len(results)):
    if results.count(results[i]) > 1:
        invalids.append(results[i])
    else:
        addresses[results[i]] = i
winners = list(set(results) - set(invalids))
if winners != []:
    print((addresses.get(max(winners)))+1)
else:
    print("none")