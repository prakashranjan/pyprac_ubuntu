import networkx as nx
import matplotlib.pyplot as plt
#import Tkinter as tk
DG = nx.DiGraph()
DG.add_edges_from([(1, 1) (1, 2), (2, 1), (1, 4), (4, 5), (2, 3), (2, 4), (3, 4)])
#print(nx.minimum_cycle_basis(DG))
#print(nx.find_cycle(DG))
xmin = 99999
minkey = None
for x in list(nx.simple_cycles(DG)):
    if len(x) < xmin:
        minkey = x
        xmin = len(x)
print(minkey)

nx.draw(DG)
plt.show()
