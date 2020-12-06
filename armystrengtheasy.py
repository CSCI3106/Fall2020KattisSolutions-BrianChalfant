# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
tc = int(input())

for _ in range(tc):
    input() # trashline
    GodzillaArmyNumber, MechaGodzillaNumber = map(int, input().split())
    GodzillaArmy = list(map(int, input().split()))
    MechaGodzillaArmy = list(map(int, input().split()))
    GodzillaArmy.sort()
    MechaGodzillaArmy.sort()
    while len(GodzillaArmy) > 0 and len(MechaGodzillaArmy) > 0:
        if GodzillaArmy[0] >= MechaGodzillaArmy[0]:
            MechaGodzillaArmy.pop(0)
        else:
            GodzillaArmy.pop(0)
    if len(GodzillaArmy) == 0:
        print("MechaGodzilla")
    else:
        print("Godzilla")