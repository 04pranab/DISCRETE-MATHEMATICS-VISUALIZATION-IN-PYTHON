import networkx as nx
import matplotlib.pyplot as plt


def draw_digraph(A):
    # Define the relation set
    relation_set = A

    # Create a directed graph
    G = nx.DiGraph()

    # Add edges from the relation set
    G.add_edges_from(relation_set)

    # Draw the graph
    pos = nx.spring_layout(G)  # Positions for all nodes

    # Nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2, arrows=True)

    # Labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    # Show the graph
    plt.title("Directed Graph from Relation Set")
    plt.axis("off")
    plt.show()
