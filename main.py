import networkx as nx
import matplotlib.pyplot as plt
from graph_generator import generate_social_network_graph, add_weights_to_edges
from graph_algorithms import bfs_paths, dfs_paths, dijkstra_shortest_path

# Generate and visualize the graph
G = generate_social_network_graph(num_users=15)
print(f"Number of nodes (users): {G.number_of_nodes()}")
print(f"Number of edges (connections): {G.number_of_edges()}")

# Visualization of the graph
fig, ax = plt.subplots(figsize=(12, 10))
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='lightgray', ax=ax)
ax.set_title(f"Social Network Graph with {G.number_of_nodes()} users and {G.number_of_edges()} connections", fontsize=16)
plt.show()

# Using DFS and BFS algorithms to find paths
start_node = list(G.nodes())[0]
goal_node = list(G.nodes())[-1]

bfs_result = list(bfs_paths(G, start_node, goal_node))
dfs_result = list(dfs_paths(G, start_node, goal_node))

print(f"BFS path: {bfs_result[0] if bfs_result else 'No path found'}")
print(f"DFS path: {dfs_result[0] if dfs_result else 'No path found'}")

# Dijkstra's algorithm for the shortest path
G_weighted = add_weights_to_edges(G)
shortest_path = dijkstra_shortest_path(G_weighted, start_node, goal_node)
print(f"Shortest path using Dijkstra: {shortest_path}")