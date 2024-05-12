from BST import BST

#
# A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties. 

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Each node (item in the tree) has a distinct key.

# 
# In a strict binary search tree (BST), each node generally has a unique value, and the tree maintains a specific ordering property: 
# all values in the left subtree of a node are less than the value of the node, 
# and all values in the right subtree are greater. This property ensures efficient search operations, such as insertions, deletions, and lookups.
negative_infinity = float('-inf')
positive_infinity = float('+inf')

def isValid(tree: BST):

    node = tree
    return isNodeValid(node)

def isNodeValid(node):
    if node == None:
        return True
    left_node = node.left
    right_node = node.right
    if left_node is not None and maxValue(left_node) >= node.value:
        return False
    if right_node is not None and minValue(right_node) <= node.value:
        return False

    return isNodeValid(left_node) and isNodeValid(right_node)

def maxValue(tree):
    if tree is None:
        return negative_infinity
  
    max_value = max(tree.value, max(maxValue(tree.left), maxValue(tree.right)))

    return max_value

def minValue(tree):
    if tree is None:
        return positive_infinity
  
    min_value = min(tree.value, min(minValue(tree.left), minValue(tree.right)))

    return min_value
    