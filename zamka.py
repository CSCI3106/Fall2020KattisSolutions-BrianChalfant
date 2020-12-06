# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020

l = int(input())
d = int(input())
x = int(input())
n = 0
m = 0


def sum_of_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum


for i in range(l, d+1):
    temp = sum_of_digits(i)
    if temp == x:
        n = i
        break

for i in range(d, -1, -1):
    temp = sum_of_digits(i)
    if temp == x:
        m = i
        break

print(n)
print(m)
