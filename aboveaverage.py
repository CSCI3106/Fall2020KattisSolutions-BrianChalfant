# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
tc = int(input())
for _ in range(tc):
    classmates = list(map(int, input().split()))
    size = classmates.pop(0)
    average = sum(classmates)/size
    print("{:.3f}%".format((len([i for i in classmates if i > average])/size) * 100))