# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import fileinput

def convert(sentence):
    oink = ""
    for word in sentence.split():
        vowels = ["a", "e", "i", "o", "u", "y"]
        pivot = 0
        if word[0] in vowels:
            oink += str(word + "yay ")
        else:
            for i in range(len(word)):
                if word[i] in vowels:
                    pivot = i
                    break
            rtnstg = word[pivot:] + word[0:pivot] + "ay "
            oink += rtnstg
    return oink

for line in fileinput.input():
    print(convert(line))