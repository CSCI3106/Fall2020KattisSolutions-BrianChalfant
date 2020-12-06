# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
RANKS = {'upper': "a", 'middle': "b", 'lower': "c"}
tc = int(input())
for _ in range(tc):
    n = int(input())
    people = {}
    longest_class = 0
    for _ in range(n):
        input_person = input().split(": ")
        input_person[1] = "".join(list(map(RANKS.get, input_person[1][0:-6].strip().split("-"))))
        if len(input_person[1]) > longest_class:
            longest_class = len(input_person[1])
        people[input_person[0]] = input_person[1]

    for person, klass in people.items():
        people[person] = (longest_class - len(klass)) * 'b' + klass
        people[person] = people[person][::-1]

    for v, k in sorted((v,k) for (k,v) in people.items()):
        print(k)
    print("=" * 30)
