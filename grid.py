# @Author Brian Chalfant 2020
# Hawaii Pacific University
# CSCI3106 - Programming Challenges - Fall 2020

from collections import deque


class Node:
    def __init__(self, row_position, col_position, dist):
        self.row = row_position
        self.col = col_position
        self.dist = dist


def bfs(source: Node, rowDest: int, colDest: int, gridlines: list, r: int, c: int, in_grid: list):
    vertexQueue = deque()
    vertexQueue.append(source)

    while len(vertexQueue) > 0:
        my_node = vertexQueue.popleft()
        if my_node.row == rowDest and my_node.col == colDest:
            return my_node.dist
        in_grid[my_node.row][my_node.col] = True
        k = gridlines[my_node.row][my_node.col]
        # Up
        newRow = my_node.row - k
        newCol = my_node.col
        if newRow >= 0:
            if not in_grid[newRow][newCol]:
                in_grid[newRow][newCol] = True
                newNode = Node(newRow, newCol, my_node.dist + 1)
                vertexQueue.append(newNode)
        # left
        newRow = my_node.row
        newCol = my_node.col - k
        if newCol >= 0:
            if not in_grid[newRow][newCol]:
                in_grid[newRow][newCol] = True
                newNode = Node(newRow, newCol, my_node.dist + 1)
                vertexQueue.append(newNode)
        # right
        newRow = my_node.row
        newCol = my_node.col + k
        if newCol < c:
            if not in_grid[newRow][newCol]:
                in_grid[newRow][newCol] = True
                newNode = Node(newRow, newCol, my_node.dist + 1)
                vertexQueue.append(newNode)
        # down
        newRow = my_node.row + k
        newCol = my_node.col
        if newRow < r:
            if not in_grid[newRow][newCol]:
                in_grid[newRow][newCol] = True
                newNode = Node(newRow, newCol, my_node.dist + 1)
                vertexQueue.append(newNode)
    return -1


rows, cols = map(int, input().split())
grid = [[0 for _ in range(cols)] for _ in range(rows)]
ingrid = [[False for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    rowValues = list(map(int, list(input())))
    for col in range(cols):
        grid[row][col] = rowValues[int(col)]
start = Node(0, 0, 0)
print(bfs(start, rows - 1, cols - 1, grid, rows, cols, ingrid))
