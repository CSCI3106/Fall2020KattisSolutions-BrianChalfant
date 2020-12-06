# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
import math

def find_dist(x, y):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

gx, gy, dx, dy = map(float, input().split())
gopher = (gx, gy)
dog = (dx, dy)
holes = []
while True:
    try:
        x, y = map(float, input().split())
        holes.append((x, y))
    except ValueError:
        break
    except EOFError:
        break

escape = False
for hole in holes:
    distance_from_gopher = find_dist(hole, gopher)
    distance_from_dog = find_dist(hole, dog)
    if distance_from_gopher * 2 < distance_from_dog:
        # escape
        print("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(hole[0], hole[1]))
        escape = True
    else:
        pass
if not escape:
    print("The gopher cannot escape.")