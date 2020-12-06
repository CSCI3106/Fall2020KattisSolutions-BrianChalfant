# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
words = list(input().split())
mydict = dict()

while len(words) > 1:
    mydict[words[1]] = words[0]
    words = list(input().split())

translation = input().strip()

while len(translation) > 0:
    oupt = mydict.get(translation)
    if oupt is None:
        print("eh")
    else:
        print(oupt)
    try:
        translation = input()
    except EOFError:
        break
