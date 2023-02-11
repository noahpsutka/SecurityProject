import matplotlib.pyplot as plt
import networkx as nx
import lightNode


G = nx.Graph()

# Adding sensors (1-4) as nodes to graph
## G.add_node(ID)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)


users = lightNode.getUsers();
# dynamically create a Graph that adds nodes from a "iterable" container (a list)
# G.add_nodes_from([users])



# Adding transactions as edges between Nodes
G.add_edge(4, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 2)
G.add_edge(2, 1)

# Shows the same graph a few different ways
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')

subax2 = plt.subplot(122)
nx.draw_shell(G,
              nlist=[range(5, 10), range(5)],
              with_labels=True,
              font_weight='bold')

# This line below was not needed on jupyter notebook
#plt.show()

# This code would give us an example graph to show off for class, but has no real connection to our data
# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
