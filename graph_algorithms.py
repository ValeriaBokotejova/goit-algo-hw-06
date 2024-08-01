import networkx as nx

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
    # Dijkstra's algorithm to find the shortest path from start to goal
    return nx.dijkstra_path(G, start, goal)