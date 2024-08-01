import networkx as nx
from faker import Faker
import random

def generate_social_network_graph(num_users=15):
    """
    Generate a social network graph with a specified number of users.
    Each user is a node, and connections (edges) are randomly created.
    """
    G = nx.Graph()
    fake = Faker()
    
    # Add nodes (users) to the graph
    users = [fake.name() for _ in range(num_users)]
    G.add_nodes_from(users)

    # Add edges (connections between users) randomly
    for i in range(num_users):
        for j in range(i + 1, num_users):
            if random.random() < 0.3:  # 30% probability that users are connected
                G.add_edge(users[i], users[j])

    return G

def add_weights_to_edges(G):
    # Add random weights to the edges of the graph. Weights represent the 'cost' or 'distance' of the connection
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)

    return G