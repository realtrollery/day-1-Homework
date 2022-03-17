# Assignment #1
# 길찾기
import random
from collections import deque

def makeGrid():
    logoLoc = [random.randint(0, vert - 1), random.randint(0, hor - 1)]
    grid[logoLoc[0]][logoLoc[1]] = 2
    for _1 in range(vert):
        for _2 in range(hor):
            if grid[_1][_2] != 2:
                grid[_1][_2] = random.randint(0,1)
    grid[0][0] = 0



def BFS(x, y):
    q.append([x, y, 0])
    grid[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]
        dist = t[2]
        print(dist)
        print(grid[ty][tx])
        for i3 in range(4):
            tempX = tx + dx[i3]
            tempY = ty + dy[i3]
            if 0 <= tempX < hor and 0 <= tempY < vert:
                if grid[tempY][tempX] == 0:
                    q.append([tempX, tempY, dist + 1])
                    grid[tempY][tempX] = 1
                if grid[tempX][tempY] == 2:
                    return dist + 1
    return -1



hor = 8
vert = 8
grid = [[1 for _ in range(hor)]for _ in range(hor)]
logoLoc = [-1,-1]
q = deque()
makeGrid()
for y in range(vert):
    print(grid[y])
print(BFS(0,0))
