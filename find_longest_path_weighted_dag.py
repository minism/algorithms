# http://community.topcoder.com/stat?c=problem_statement&pm=1593&rd=4494

# Find the longest path in a weighted DAG

# Procedure:
#   - Toposort the dag
#   - Step through each vertex and set its total_cost = 
#       max(incoming_neighboor + incoming_edge) for all neighboors
#   - Return highest cost found in graph

import collections


def toposort(G):
    result = []
    queue = collections.deque()
    starting_nodes = [True] * len(G)
    for edges in G:
        for v in edges:
            starting_nodes[v] = False
    for i in range(len(starting_nodes)):
        if starting_nodes[i]:
            queue.appendleft(i)

    inserted = {}
    while len(queue) > 0:
        curr = queue.pop()
        result.append(curr)
        for v in G[curr]:
            if not inserted.get(v):
                inserted[v] = True
                queue.appendleft(v)

    return result


def find_longest_path(adj_list, cost_list):
    G = map(lambda s: map(int, s.split()), adj_list)
    C = map(lambda s: map(int, s.split()), cost_list)
    
    # Cache incoming vertices and costs
    incoming = {}
    for i, edges in enumerate(G):
        for j, outgoing in enumerate(edges):
            cost = C[i][j]
            incoming.setdefault(outgoing, []).append((i, cost))

    max_costs = {}
    max_total_cost = 0
    for v in toposort(G):
        max_incoming_cost = 0
        if len(incoming.get(v, [])) > 0:
            for inc, cost in incoming[v]:
                cost = max_costs.get(inc, 0) + cost
                if cost > max_incoming_cost:
                    max_incoming_cost = cost
        max_costs[v] = max_incoming_cost
        if max_incoming_cost > max_total_cost:
            max_total_cost = max_incoming_cost
    
    return max_total_cost

# ex0
print find_longest_path(['1 2', '2', ''], ['5 3', '7', ''])

# ex1
print find_longest_path(["1 2 3 4 5","2 3 4 5","3 4 5","4 5","5",""],
                        ["2 2 2 2 2","2 2 2 2","2 2 2","2 2","2",""])

# ex4
print find_longest_path(["","2 3","3 4 5","4 6","5 6","7","5 7",""],
                        ["","30 50","19 6 40","12 10","35 23","8","11 20",""])
