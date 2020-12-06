# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n, t = map(int, input().split())
bank = []
for i in range(t+1):
    bank.append([])
for i in range(n):
    money, leave = map(int, input().split())
    bank[leave].append(money)
total = 0
decisions = []
for i in range(t, -1, -1):
    decisions += bank[i]
    decisions.sort()
    if decisions:
        total += decisions.pop(len(decisions)-1)
print(total)