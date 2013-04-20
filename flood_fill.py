import sys
import collections


size = 8
table = []
for i in range(size):
    table.append([])
    for j in range(size):
        table[i].append(False)


for i in range(size):
    table[i][4] = True



def floodFill(G, x, y):
    Q = collections.deque()
    Q.appendleft((x,y))
    while len(Q) > 0:
        x, y = Q.pop()
        G[x][y] = True
        neighboors = []
        if x > 0:
            neighboors.append((x-1, y))
        if x < size - 1:
            neighboors.append((x+1, y))
        if y > 0:
            neighboors.append((x, y-1))
        if y < size - 1:
            neighboors.append((x, y+1))
        for nx, ny in neighboors:
            if not G[nx][ny]:
                Q.appendleft((nx,ny))



floodFill(table, 2,2)


# Print table
for i in range(size):
    for j in range(size):
        sys.stdout.write(table[i][j] and 'X ' or 'O ')
    sys.stdout.write('\n')
