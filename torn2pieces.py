# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020
from collections import deque
def bfs(graph, start, goal):
    # keep track of explored nodes
    explored = []
    queue = deque()
    queue.append([start])
    if start == goal:
        return start
    while queue:
        try:
            # pop the first path from the queue
            path = queue.popleft()
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                adjacency_list = graph[node]
                for adjNode in adjacency_list:
                    new_path = list(path)
                    new_path.append(adjNode)
                    queue.append(new_path)
                    # return path if adjnode is goal
                    if adjNode == goal:
                        return " ".join(new_path)
                explored.append(node)
        except:
            return"no route found"
    return "no route found"


tc = int(input())
build_graph = {}
vertices = []
edges = []
for i in range(tc):
    line = input().split()
    origin = line[0]
    for connection in line[1:]:
        edges.append((origin, connection))
        edges.append((connection, origin))
startingVertex, destinationVertex = input().split()

for s, d in edges:

    if s not in build_graph:
        build_graph[s] = []
    build_graph.get(s).append(d)

print(bfs(build_graph, startingVertex, destinationVertex))