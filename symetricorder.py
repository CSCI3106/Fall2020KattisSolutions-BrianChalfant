# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
sets = 1
while n != 0:
    cycle = n

    names = []
    for _ in range(cycle):
        names.append(input().strip())
    print("SET " + str(sets))
    new_order = names[::2] + names[1::2][::-1]
    for i in range(len(new_order)):
        print(new_order[i])
    sets += 1
    n = int(input())