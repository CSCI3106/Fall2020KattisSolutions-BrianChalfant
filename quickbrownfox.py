# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import string
for _ in range(int(input())):
    alpha = set(string.ascii_lowercase)
    letter = input().lower()
    accounted_for = set(filter(lambda x: x.isalpha(), letter))
    if len(accounted_for) == len(alpha):
        print("pangram")
    else:
        print("missing " + ''.join(sorted(alpha - accounted_for)))