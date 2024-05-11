from BST import BST

#
# A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties. 

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Each node (item in the tree) has a distinct key.

def isValid(tree: BST):

def isValid(tree: BST):
    return isNodeValid(tree, float('-inf'), float('inf'))

def isNodeValid(node, min_value, max_value):
    if node is None:
        return True
    if not min_value < node.value < max_value:
        return False
    return isNodeValid(node.left, min_value, node.value) and isNodeValid(node.right, node.value, max_value)

