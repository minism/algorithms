# Dijstraks algorithm
# Used against graph represented by adjacency matrix



def dijkstra(G, start, end):
    data = [{
        'distance': None,
        'visited': False,
    } for n in range(len(G))]
    curr = start
    data[0]['distance'] = 0

    # Get unvisited neighboors
    while True:
        print curr
        next_node, min_value = None, None
        curr_distance = data[curr]['distance']
        for vertex, cost in enumerate(G[curr]):
            if cost >= 0 and not data[vertex]['visited']:
                new = curr_distance + cost
                if not data[vertex]['distance'] or new < data[vertex]['distance']:
                    data[vertex]['distance'] = new
                if not min_value or data[vertex]['distance'] < min_value:
                    next_node = vertex
                    min_value = data[vertex]['distance']
        data[curr]['visited'] = True
        if curr == end:
            return
        curr = next_node


graph = [
    [-1,  7,  9, 14, -1, -1],
    [ 7, -1, 10, -1, -1, 15],
    [ 9, 10, -1,  2, -1, 11],
    [14, -1,  2, -1,  9, -1],
    [-1, -1, -1,  9, -1,  6],
    [-1, 15, 11, -1,  6, -1],
]

dijkstra(graph, 0, 4)
