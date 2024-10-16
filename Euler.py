import networkx as nx

# Define the relation set
relation_set = {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}

# Create a directed graph
G = nx.DiGraph()

# Add edges from the relation set
G.add_edges_from(relation_set)

# Check if an Euler circuit exists
is_euler_circuit = nx.is_eulerian(G)

# Check if an Euler path exists
is_euler_path = nx.is_eulerian(G.to_undirected())

# Print the result
if is_euler_circuit:
    print("An Euler circuit exists in the graph.")
elif is_euler_path:
    print("An Euler path exists in the graph.")
else:
    print("Neither an Euler circuit nor an Euler path exists in the graph.")
