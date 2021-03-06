import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import student_utils_sp18 as student 
from networkx import *
import sys
import random

#generate a graph
n= 200
G=fast_gnp_random_graph(n, 0.4)


#read a graph, input path, doesnt work
# G2 = read_graphml("./graphs/50TestModified.graphml")

def create_adjacency_matrix(G):
	n = len(G)
	for u,v,d in G.edges(data=True):
		d['weight'] = random.randint(1,11)

	shortest = dict(nx.floyd_warshall(G))

	adj_m = [[0 for x in range(n)] for y in range(n)]

	for u, v, datadict in G.edges(data=True):
		if datadict['weight'] > shortest[u][v]:
			datadict['weight'] = shortest[u][v]

		adj_m[u][v] = datadict['weight']
		adj_m[v][u] = datadict['weight']

	for i in range(len(adj_m)):
		for j in range(len(adj_m[0])):
			if(i==j):
				adj_m[i][j] = random.randint(1,11)
			
			if(adj_m[i][j] == 0):
				adj_m[i][j] = 'x'
	return adj_m

def create_file(n, adj_list):
	f = open("./input_output_files/test.in", "w")
	f.write(str(n)+"\n")

	for i in range(n):
		f.write(str(i))
		if(i != n-1):
			f.write(" ")

	f.write("\n")
	f.write(str(0) + "\n")
	for i in range(len(adj_list)):
		for j in range(len(adj_list[0])):
			f.write(str(adj_list[i][j]))
			if(j != len(adj_list[0]) - 1):
				f.write(" ")
		if(i != len(adj_list) - 1):
			f.write("\n")

	f.close()



print(create_adjacency_matrix(G2))

adj_m = create_adjacency_matrix(G)
create_file(n, adj_m)

nx.write_gexf(G, "./graphs/test.gexf")




