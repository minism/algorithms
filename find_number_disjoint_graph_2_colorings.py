# Problem: Marketing
# http://community.topcoder.com/stat?c=problem_statement&pm=1524&rd=4472

# We implement the solution as follows:
#   Consider the product set as a disjoint union of graphs.
#
#   A subset of products can be marketed successfully if the products can
#   be distributed into two sets such that no pair exists in the same set.  In other
#   words, only if its graph is bipartite.
#
#   For each graph, determine if it is bipartite by attempting to 2-color it.  
#   If the graph is not bipartite, then we return False
#
#   Finally, for each graph, there are two ways to color the graph (by inverting the colors:
#   or this can be thought of as inverting one color and propogating the change to restore
#   the coloring condition), and thus there are two ways to group the products
#
#   Therefore, we return 2 ^ N, where N is the number of graphs

import collections


def howMany(products):
    # Color/visited table
    # 0 = unvisited, 1 = red, 2 = black
    colors = [0] * len(products)
    num_graphs = 0

    # Iterate through each unvisited node, which will give us each individual graph
    for i in range(len(products)):
        if colors[i] > 0:
            continue

        # Reached a new graph
        num_graphs += 1

        # BFS the graph and attempt to 2-color it (test for bipartiteness)
        queue = collections.deque()
        color = 1
        colors[i] = color
        queue.appendleft(i)
        while len(queue) > 0:
            curr = queue.pop()
            next_color = colors[curr] % 2 + 1
            for neighboor in map(int, products[curr].split()):
                if colors[neighboor] > 0:
                    if colors[neighboor] != next_color:
                        return -1
                else:
                    colors[neighboor] = next_color
                    queue.appendleft(neighboor)

    # All graphs are bipartite, return the number of ways they can all be colored
    return 2 ** num_graphs



# ex 0
print howMany(['1 4', '2', '3', '0', ''])

# ex 1
print howMany(['1', '2', '0'])

# ex 2
print howMany(['1', '2', '3', '0', '0 5', '1'])

# ex 3
print howMany([''] * 30)
