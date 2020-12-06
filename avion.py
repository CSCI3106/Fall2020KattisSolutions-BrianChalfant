# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
bn = []
result = []
while True:
    try:
        n = input()
        if n == '':
            break
        else:
            bn.append(n)
    except EOFError:
        break
for i in range(len(bn)):
    if "FBI" in bn[i]:
        result.append(str(i + 1))

if len(result) > 0:
    print(" ".join(result))
else:
    print("HE GOT AWAY!")
