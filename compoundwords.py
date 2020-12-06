# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
words = []
permutations = set()

line = input().split()
while line != []:
    words.extend([*line])
    try:
        line = input().split()
    except ValueError:
        break
    except EOFError:
        break

for word1 in words:
    for word2 in words:
        if word1 == word2:
            pass
        else:
            permutations.add(word1+word2)

for word in sorted(permutations):
    print(word)