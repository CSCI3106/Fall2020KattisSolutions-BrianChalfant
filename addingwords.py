# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import sys
definitions = {}
for i in sys.stdin:
    if i.startswith("def"):
        variable, value = i.strip().split()[1:]
        definitions[variable] = value
    elif i.startswith("calc"):
        symbols = i.strip().split()[1:-1]
        if any(x not in definitions for x in symbols[::2]):
            print(i[5:].strip() + " unknown")
        else:
            equation = list(map(lambda x: definitions.get(x, x), symbols))
            result = eval(" ".join(equation))
            backwards = {v: k for k, v in definitions.items()}
            print(i[5:].strip() + " " + backwards.get(str(result), "unknown"))
    else:
        definitions.clear()