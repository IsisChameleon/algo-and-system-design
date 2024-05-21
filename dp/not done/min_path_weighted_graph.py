"""
Given a graph (Number of edges, number of nodes, From and To node pairs), you need to find the minimum weighted path from the first node(1) 
to the last node(N) and return it’s weight. 
If there exists no edge between any two vertices which would be required to complete the path from the first to the last node, 
then an edge can be created between them with the weight 1.
"""

# Approach:
# - Create a graph using the given number of nodes and edges.
# - Create a queue and push the first node into it.
# - Create a visited array and mark the first node as visited.
# - Create a distance array and mark the first node as 0.
# - While the queue is not empty, pop the top element of the queue and push all the unvisited neighbors of the popped element into the queue.
# - Mark the popped element as visited and update the distance of the neighbors.
# - If the popped element is the last node, return the distance of the last node.
# - If the queue is empty and the last node is not visited, then return -1.
# - If the queue is empty and the last node is visited, then return the distance of the last node.
# - If the queue is empty and the last node is not visited, then return -1.
# - If the queue is empty and the last node is visited, then return the distance of the last node.
# - If the queue is empty and the last node is not visited, then return -1.
# - If the queue is empty and the last

from typing import List
import networkx as nx

G = nx.DiGraph()
G.add_edges_from(
[('A', 'B', { 'w' : 0.1 }), ('A', 'C', { 'w' : 0.2 }), ('D', 'B', { 'w' : 0.5 }), ('E', 'C', { 'w' : 0.6 }), ('E', 'F', { 'w' : 0.1 }),
('B', 'H', { 'w' : 0.3 }), ('B', 'G', { 'w' : 0.9}), ('B', 'F', { 'w' : 0.1 }), ('C', 'G', { 'w' : 0.7 })])

"""
https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/
For the graph templates, assume the nodes are numbered from 0 to n - 1 and the graph is given as an adjacency list. 
Depending on the problem, you may need to convert the input into an equivalent adjacency list before using the templates.
"""

class Node:
    def __init__(self, weight: int, neighbours: List['Node']):
        self.weight = weight
        self.neighbours = neighbours


def min_path_weighted_graph(G: nx.DiGraph):

    # create a digraph with networkx
    pass