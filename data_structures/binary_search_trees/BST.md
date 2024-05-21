# BST

A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties. 

. The left subtree of a node contains only nodes with keys less than the node’s key.  

. The right subtree of a node contains only nodes with keys greater than the node’s key.  

. Both the left and right subtrees must also be binary search trees.  

. Each node (item in the tree) has a distinct key (no duplicate nodes)

Can accomodate same keys, usually to the right or else as an additional counter with each node.

## Key operations on BSTs


### 1. Insertion  

To insert a new key, start from the root and compare the key to be inserted with the current node's key. Recursively place the key into the left subtree if it is less than the current node, or into the right subtree if it is greater. 
Time complexity in the worst case is O(n), but on average, it's O(log n).

### 2. Search

Begin at the root and compare the search key to the key in the current node. 
Recursively search in the left or right subtree following the same rules as insertion. 
This operation also has a time complexity of O(log n) on average.

### 3. Deletion  

 This is more complex and comes in three cases:
    Node with no child: Simply remove the node.
    Node with one child: Remove the node and replace it with its subtree.
    ode with two children: Find the in-order successor of the node, copy its value to the node, and delete the in-order successor. This last case ensures the properties of the BST are maintained.

### 4. Traversal  

Traversal operations in a binary search tree (BST) or any tree data structure involve visiting each node in the tree in a specific order. Each traversal order serves different purposes and is useful in various applications. The most common types of tree traversal methods are:

#### 4.1. In-Order Traversal (Left, Root, Right)  

Process: Visit the left subtree, then the current node (root), and finally the right subtree.

Purpose: This traversal yields nodes in a non-decreasing order for BSTs because it accesses elements in their logical order from smallest to largest. It's commonly used to sort elements and to visually inspect the structure of a BST.

Applications: Sorting operations, binary tree printing in order, converting a BST to a sorted list.

#### 4.2. Pre-Order Traversal (Root, Left, Right)

Process: Visit the current node first, then traverse the left subtree, and finally the right subtree.

Purpose: This traversal is used when you need to explore roots before inspecting leaves. It's useful for creating a copy of the tree or to serialize a binary tree for storage or transmission, as it captures the structure exactly from the top down.

Applications: Tree copying, serialization, and other operations where tree structure replication is necessary.

#### 4.3. Post-Order Traversal (Left, Right, Root)  

Process: Visit the left subtree, then the right subtree, and finally the current node. 

Purpose: This traversal is useful for operations that require a node to be processed after its descendants (for instance, when recursively calculating the size or depth of the tree). It is also used in safely deleting nodes from the tree.

Applications: Tree deletion, calculating used space in file systems (if directories and files are represented as trees), post-processing on a tree.

#### 4.4. Level-Order Traversal (Breadth-First)  

Process: Visit nodes level by level from the root downwards.  

Purpose: This traversal is used when you need to explore the tree layer by layer. It is used in scenarios like breadth-first search (BFS), where the shortest path in unweighted graphs is required, or when printing the tree level by level.

Applications: BFS in graphs, finding the shortest path in unweighted trees, generating a visual representation of the tree.


## Balanced BSTs

To ensure that BST operations remain efficient even in the worst-case scenarios, self-balancing BSTs such as AVL Trees, Red-Black Trees, and Splay Trees are used. These trees adjust themselves during insertions and deletions to maintain a low height, ensuring that the time complexity of operations does not degrade to O(n).

A balanced BST specifically tries to maintain a condition where the difference in heights between the left and right subtrees at any node is minimal. This balance helps prevent the BST from degrading into a structure similar to a linked list, which would result in operations taking linear time (O(n)) rather than logarithmic time (O(log n)).

Complexity:

Time Complexity: For a balanced BST, average and worst-case time complexity for search, insertion, and deletion operations are O(log n). 
In an unbalanced BST (which resembles a linked list), these operations can degrade to O(n).

Space Complexity: O(n), where n is the number of nodes in the tree.

## Real world use cases


1. Database Indexing  

BSTs are extensively used in database systems to index data, which helps speed up the retrieval of records. B-trees and B+ trees, which are variants of BSTs, are particularly common for this purpose. They allow databases to store and manage large amounts of data efficiently, providing quick access to records through operations like SQL queries that can perform range searches, exact matches, and more.

2. File Systems  

In file systems, BSTs are used to manage and store file information. File directories and their contents can be stored in a BST, allowing quick access, addition, and deletion of files. The file system's efficiency in locating files through their paths or searching files based on attributes like size or type relies heavily on the underlying data structure, often a form of BST.

3. Autocomplete Features  

BSTs are utilized in implementing autocomplete functionality in search engines, text editors, or IDEs (Integrated Development Environments). By storing the sorted dictionary of words or tokens in a BST, the system can quickly suggest completions as the user begins typing, efficiently narrowing down the list of suggestions based on the input prefix.

4. Network Routing Table

Routing tables in networks can be structured as BSTs to manage and lookup network addresses and routes efficiently. This is crucial in networking where routers need to find the next hop addresses quickly. The BST helps in keeping the table sorted and allows quick updates and retrievals, which is essential for high-performance networking.

5. Graphics Rendering 

In computer graphics, particularly in applications involving ray tracing, spatial data structures such as BSP trees (Binary Space Partitioning trees, a relative of BSTs) are used. These trees help in organizing objects in the graphical space to minimize the number of calculations needed to determine which objects need to be rendered. This is crucial for performance in video games and simulations where rendering speed is critical.

6. Memory Management

BSTs are useful in memory management within operating systems to manage available blocks of memory.

7. Decision Support Systems

BSTs are also integral in various decision support systems, where large datasets need to be queried and analyzed quickly. BSTs can help optimize searches across configurations or parameters to find the best solutions or decisions based on multiple criteria.

Conclusion
These examples illustrate the versatility and importance of BSTs across different domains, highlighting their role in optimizing operations that require fast data retrieval and management. Their ability to balance and sort data makes them indispensable in both theoretical computer science education and practical software development tasks.