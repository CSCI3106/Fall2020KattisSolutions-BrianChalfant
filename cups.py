# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
cups = {}
for _ in range(n):

    cup_n_color = input().split()
    if cup_n_color[0].isnumeric():
        # Radius is doubled
        cups[cup_n_color[1]] = (int(cup_n_color[0])//2)
    else:
        # Radius is not doubled
        cups[cup_n_color[0]] = int(cup_n_color[1])

for cup in sorted(cups.items(), key=lambda x: x[1]):
    print(cup[0])