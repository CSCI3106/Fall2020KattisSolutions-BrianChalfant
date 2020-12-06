# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
tc = int(input())

for _ in range(tc):
    input() # trashline
    GodzillaArmyNumber, MechaGodzillaNumber = map(int, input().split())
    NGodzillaArmy = list(map(int, input().split()))
    NMechaGodzillaArmy = list(map(int, input().split()))
    NGodzillaArmy.sort()
    NMechaGodzillaArmy.sort()
    if NGodzillaArmy[-1] >= NMechaGodzillaArmy[-1]:
        print("Godzilla")
    elif NMechaGodzillaArmy[-1] > NGodzillaArmy[-1]:
        print("MechaGodzilla")
    else:
        print("uncertain")