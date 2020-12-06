# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
h, m = map(int, input().split())
if m > 45:
    print("{} {}".format(h,(m-45)))
else:
    m = 60 + (m-45)
    if h == 0:
        h = 23
    else:
        h -= 1
    print("{} {}".format(h,m))