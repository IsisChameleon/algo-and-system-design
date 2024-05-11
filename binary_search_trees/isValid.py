from BST import BST

#
# A Binary Search Tree (BST) is a node-based binary tree data structure that has the following properties. 

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Each node (item in the tree) has a distinct key.

def isValid(tree: BST):

    node = tree
    return isNodeValid(node)

def isNodeValid(node):
    left_node = node.left
    right_node = node.right
    if left_node.value >= node.value:
        return False
    if right_node.value < node.value:
        return False
    if node == None:
        return True
    return isNodeValid(left_node) and isNodeValid(right_node)

