# Definition 

A Min Heap is a fundamental data structure that's especially useful in scenarios where you frequently need to retrieve the smallest element from a set of data. It's a type of binary heap that satisfies the heap property, where the value of each node is less than or equal to the values of its children. This property makes the root the minimum element of the heap. Min Heaps are widely discussed in technical interviews due to their utility in various algorithms, including heap sort, and in constructing efficient priority queues.

# Key Characteristics of Min Heaps:

Complete Binary Tree: A min heap is a complete binary tree; that is, all levels are fully filled except possibly for the last level, which is filled from left to right. This structure is usually maintained as an array for efficiency.
Heap Property: In a min heap, for any given node 𝐶 with a parent 𝑃, the value of 𝑃 <= 𝐶. This property ensures that the smallest element is always at the root of the tree.  

# Key Characteristics of Max Heaps:

Complete Binary Tree: A Max Heap is also a complete binary tree, which means that all levels are completely filled except possibly for the last level, which is filled from left to right.
Heap Property: The key property of a Max Heap is that the value of each node is greater than or equal to the values of its children. This guarantees that the largest value is at the base of the heap, easily accessible.


# Basic Operations:


## Insertion (O(log n)):  
To insert a new element into a min heap:

Add the Element at the End: Start by adding the element at the end of the heap (maintaining the complete tree property).
Heapify Up: Adjust the heap by comparing the added element with its parent; swap if the parent is larger. Repeat this step until the heap property is restored.

## Removal of the Minimum (O(log n)):
To remove the root (minimum element) from a min heap:

Replace the Root: Replace the root with the last element in the heap.
Heapify Down: Adjust the heap from the root downwards. Compare the new root with its children and swap it with the smaller child until the heap property is restored.

## Find Minimum (O(1)):
The minimum element can always be found at the root of the heap, which is the first element of the array that represents the heap.

## Build a Min Heap (O(n)):  
Given an unsorted array, you can build a min heap by arranging the elements to satisfy the min heap property:

Start from the first index which has a child (last non-leaf node)
Apply the heapify down process from each non-leaf node all the way up to the root.

# Practical Applications:

Priority Queues: Min heaps are ideal for priority queues where you need to frequently access the smallest item.
Heap Sort: You can sort items by repeatedly removing the smallest element from a min heap.
Graph Algorithms: Used in Dijkstra's algorithm and Prim's algorithm for finding the shortest path and minimum spanning tree, respectively.