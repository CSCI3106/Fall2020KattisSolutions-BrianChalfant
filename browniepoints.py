# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
n = int(input())
while n != 0:
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    origin = coords[(len(coords) - 1) // 2]
    recentered_points = [(p[0] - origin[0], p[1] - origin[1]) for p in coords]

    ollie_points = 0
    stan_points = 0
    for (x, y) in recentered_points:
        if x == 0 or y == 0:
            pass
        else:
            if x > 0 and y > 0:
                stan_points += 1
            elif x < 0 and y < 0:
                stan_points += 1
            else:
                ollie_points += 1

    print(stan_points, ollie_points)
    n = int(input())