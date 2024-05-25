"""
Given a graph (Number of edges, number of nodes, From and To node pairs), you need to find the minimum weighted path from the first node(1) 
to the last node(N) and return it’s weight. 
If there exists no edge between any two vertices which would be required to complete the path from the first to the last node, 
then an edge can be created between them with the weight 1.
"""

"""
Tabnine:

Given a graph (Number of edges, number of nodes, From and To node pairs), you need to find the minimum weighted path from the first node(1) 
to the last node(N) and return it’s weight. 
If there exists no edge between any two vertices which would be required to complete the path from the first to the last node, 
then an edge can be created between them with the weight 1.

1. Graph Representation: Use an adjacency list to represent the graph.
2. Initialize Data Structures:

    A priority queue to keep track of the nodes to be processed.
    A distance array to store the minimum distance from the start node to each node.
    A set to keep track of visited nodes.

3. Dijkstra's Algorithm:
    Start from the first node (1).
    For each node, update the distances to its neighbors.
    If a node is not directly connected to another node, consider the edge with weight 1.

4. Return the Result: The distance to the last node (N) will be the result. If the last node is not reachable, return -1.

"""

import heapq


def min_path_weighted_graph(num_nodes: int, edges: List[Tuple[int, int, int]]) -> int:

# 1. setup data structures
#--------------------------
        graph = [[] for _ in range(num_nodes)]

# done in an array when the node number is 1...N contiguous integer number otherwise hashmap
        for source_node, dest_node, distance in edges:
            graph[source_node].append((dest_node, distance))
            graph[dest_node].append((source_node, distance))

        visited = [False] * num_nodes  # nodes already visisted
        distance = [float('inf')] * num_nodes # distance from node 0 to node i

# 2. Initial values/Base case
#-------------------------------

        distance[0] = 0


# 3. Setup first node to visit
#--------------------------------

        priority_queue = [(0, 0)]  # (distance, node) first tuple element needs to be distance because that's going to 
                                  # be what is used for the min heap

        
# 4. Dijkstra's Algorithm
#--------------------------

# the pop(0) and append operations make it a FIFO (First-In-First-Out) queue.
# append: adds elements to the end of the list.
# pop(0): removes elements from the beginning of the list.

        while priority_queue:
                dist, node = heapq.heappop(priority_queue) #<-------- pay attention pop(0) not pop 

                if visited[node]:
                    continue

                visited[node] = True

                for neighbor, weight in graph[node]:
                    if not visited[neighbor]:
                        # for each non visited neighbor, calculate the distance from current node to neighbour
                        # if that distance is smallest that any previous distance calculated to that neighbour ndoe
                        # we keep the new minimum and update the distance[neibhbour] with the new value
                        new_dist = dist + weight
                        if new_dist < distance[neighbor]:
                            distance[neighbor] = new_dist
                            heapq.heappush(priority_queue, (new_dist, neighbor))

        if distance[num_nodes - 1] == float('inf'):
            return -1 # means we never did reach the last node

        return distance[num_nodes - 1]


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

from typing import List, Tuple
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