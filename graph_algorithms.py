import heapq

def bfs_paths(G, start, goal):
    # Breadth-First Search (BFS) to find all paths from start to goal. Yields each path found
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(G.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def dfs_paths(G, start, goal):
    # Depth-First Search (DFS) to find all paths from start to goal. Yields each path found
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(G.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def dijkstra_shortest_path(G, start, goal):
    # Custom implementation of Dijkstra's algorithm
    shortest_paths = {vertex: (float('infinity'), []) for vertex in G}
    shortest_paths[start] = (0, [start])
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex == goal:
            break

        for neighbor, attributes in G[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor][0]:
                shortest_paths[neighbor] = (distance, shortest_paths[current_vertex][1] + [neighbor])
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths[goal][1], shortest_paths[goal][0]