import networkx as nx
import matplotlib.pyplot as plt
import math

def create_grid_graph(m, n):
    G = nx.Graph()
    num_vertices = m * n + 1
    label_k = math.ceil((num_vertices) / 2)
    k = math.ceil((num_vertices) / 2) / (n - 1)
    resuidual = k
    edge_weights = set()
    labels = [1]

    
    for i in range(1, n+1):
        G.add_edge(0, 1)
        edge_weights.add(1 + 1)
        if i == 1:
            labels.append(1)
        if i != 1:
            vertex_label = int(resuidual)
            G.add_edge(0, i)
            labels.append(vertex_label)
            edge_weights.add(1 + int(resuidual))
            resuidual = resuidual + k

    edge_weight = 2
    
    for i in range(1, n+1):
        for j in range(1, m):
            child_vertex = n + j + (m - 1) * (i - 1)
            G.add_edge(i, child_vertex)
            assigned = False
            while not assigned:
                if edge_weight not in edge_weights:
                    edge_weights.add(edge_weight)
                    child_vertex_label = edge_weight - labels[i]
                    labels.append(child_vertex_label)
                    assigned = True
                edge_weight += 1
    print("Value of max label", label_k)
    print("Vertex Labels" ,labels)
    print("Edge Weights", edge_weights)
    print("Edge weights length", len(edge_weights))
    print("Expected Edge weight length", num_vertices -1 )
    return G, labels


m = 4
n = 12
grid_graph, labels = create_grid_graph(m, n)

pos = nx.spring_layout(grid_graph)
nx.draw(grid_graph, pos, with_labels=True, labels={i: label for i, label in enumerate(labels)}, node_size=500, node_color="skyblue", font_size=10)

plt.title(f"{m}x{n} Grid Graph")
plt.show()