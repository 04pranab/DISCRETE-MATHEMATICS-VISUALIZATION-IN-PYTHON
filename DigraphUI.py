import tkinter as tk
import tkinter.messagebox as msg
import networkx as nx
import matplotlib.pyplot as plt
import random as rn

# Function to draw a directed graph using networkx
def draw_digraph(lt):
    relation_set = [(lt[i], lt[i+1]) for i in range(0, len(lt)-1, 2)]  # Creating pairs of edges
    G = nx.DiGraph()
    G.add_edges_from(relation_set)
    
    pos = nx.spring_layout(G)  # Layout for node positions
    
    # Draw the graph components
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=3, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    plt.title("Directed Graph from Relation Set")
    plt.axis("off")  # Hide axes
    plt.show()

# Function triggered by the button click
def draw():
    try:
        l = int(list_entry.get())
        lt = []
        if l < 2:
            raise ValueError("Insufficient vertices to form edges.")
        for i in range(l):
            lt.append(rn.randint(1, l))
        draw_digraph(lt)  # Call the graph drawing function
    except ValueError as ve:
        msg.showerror("Error", str(ve))

# Set up the tkinter GUI
root = tk.Tk()
root.geometry("600x500+750+300")
root.title("Random DiGraphs")

name_label = tk.Label(root, text="Random DiGraphs", font=("Arial", 25))
name_label.pack()

info_label = tk.Label(root, text="Enter Vertices (normal text)", font=("Arial", 12))
info_label.pack()

list_entry = tk.Entry(root, width=50, font=10)
list_entry.pack()

enter_button = tk.Button(root, text="Enter", width=50, height=1, font=("Arial", 12), command=draw)
enter_button.pack()

root.mainloop()
