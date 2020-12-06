# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
s, t, n = input().split()
s = int(s)
t = int(t)
n = int(n)
userString = input().split()
di = [int(i) for i in userString]
userString = input().split()
bi = [int(i) for i in userString]
userString = input().split()
ci = [int(i) for i in userString]
timeAlotted = t - s
timeConsumed = 0
for i in range(n):
    timeConsumed += di[i]
    timeConsumed += (ci[i] - di[i])
    timeConsumed += bi[i]
timeConsumed += di[n]
if timeConsumed > timeAlotted:
    print("no")
else:
    print("yes")