import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import student_utils_sp18 as student 
from networkx import *
import sys
import random

n= 50
e = 580

G=fast_gnp_random_graph(n, 0.4)
# some properties

#print("node degree clustering")
#for v in nodes(G):
 #   print('%s %d %f' % (v,degree(G,v),clustering(G,v)))

# print the adjacency list to terminal
#try:
 #   write_adjlist(G,sys.stdout)
#except TypeError: # Python 3.x
 #   write_adjlist(G,sys.stdout.buffer)

A = nx.adjacency_matrix(G)


for u,v,d in G.edges(data=True):
	d['weight'] = random.randint(1,11)

shortest = dict(nx.floyd_warshall(G))

for u, v, datadict in G.edges(data=True):
	if datadict['weight'] > shortest[u][v]:
		datadict['weight'] = shortest[u][v]




def create_file(A):
	with open('TESTER.txt','w') as f:
		for line in A:
			np.savetxt(f, line, fmt='%.2f')
	f.close()


<<<<<<< HEAD
nx.draw(G)
nx.write_gexf(G, "./graphs/textWeights.gexf")

=======

nx.draw(G)
nx.write_gexf(G, "./graphs/50node.gexf")
>>>>>>> 1069a5e0f902b60e17c17b6afd2819ea9eb0dded
