# Escape: Division I l2 problem
# http://community.topcoder.com/stat?c=problem_statement&pm=1170&rd=4371

# Thoughts: Could solve using dijkstra, however A* would should be more
# efficient since we know the general vector is northeast

# We'll use a simple static weighted node cost function, f(n) = g(n) + (W + 1) * h(n)

# We'll need to use Priority Queue (heapq) to store next nodes to visit

# We will use a tilemap-like matrix to represent the graph

import sys
import copy
import time
import heapq
import math

def render(matrix, costs, x, y):
    out = sys.stdout    
    for row, cols in enumerate(matrix):
        for col, cell in enumerate(cols):
            if col == x and row == y:
                out.write('$'.ljust(2))
            elif costs.has_key((col, row)):
                cost = int(costs[(col, row)])
                out.write(str(cost).ljust(2))
            elif cell < 0:
                out.write('X'.ljust(2))
            else:
                out.write('-'.ljust(2))
        out.write('\n')


def weighted_a_star(matrix, start, goal):
    g_costs = {} 
    f_costs = {}
    pq = []
    heapq.heappush(pq, [0, start[0], start[1]])
    g_costs[start] = 0

    # Heuristic function
    def h(x, y):
        return abs(x-goal[0]) + abs(y-goal[1])

    while len(pq) > 0:
        fcost, x, y = heapq.heappop(pq) 
        render(matrix, f_costs, x, y)

        # Calculate cost of valid neighbors and put on heapq
        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if nx < 0 or nx > len(matrix) or ny < 0 or ny > len(matrix[0]):
                continue
            if f_costs.get((nx,ny)):
                continue
            weight = 0
            gcost = g_costs[x, y] + 1
            fcost = gcost + (weight + 1) * h(nx, ny)
            g_costs[(nx, ny)] = gcost
            f_costs[(nx, ny)] = fcost
            heapq.heappush(pq, [fcost, nx, ny])

        time.sleep(1)

matrix = [[0] * 10 for i in range(10)]
matrix[4][4] = -1
matrix[4][5] = -1
matrix[4][6] = -1
matrix[5][4] = -1
matrix[5][5] = -1
matrix[5][6] = -1
matrix[6][4] = -1
matrix[6][5] = -1
matrix[6][6] = -1

weighted_a_star(matrix, (1, 9), (8, 8))
