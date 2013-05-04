# Determine if a graph is bitartite by attempting to 2-color the graph
import collections
import random


def is_bipartite(G):
    # Store vertex colors (also gives us visited state!)
    colors = {}

    # BFS graph, alternating colors
    queue = collections.deque()
    init = random.choice(G.keys())
    colors[init] = 0
    queue.appendleft(init)
    while len(queue) > 0:
        curr = queue.pop()
        next_color = (colors[curr] + 1) % 2
        for neighboor in G[curr]:
            if colors.get(neighboor):
                if colors[neighboor] != next_color:
                    return False
            else:
                colors[neighboor] = next_color
                queue.appendleft(neighboor)
    return True


# Adjacency list of graph
graph = {
    0: [4,5],
    1: [4],
    2: [3,5],
    3: [0],
    4: [2,1],
    5: [],
}

print is_bipartite(graph)
