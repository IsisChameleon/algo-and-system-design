from BST import BST

# In-Order Traversal (LNR): Left subtree, Node, Right subtree
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

# Pre-Order Traversal (NLR): Node, Left subtree, Right subtree
def preorder_traversal(root):
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

# Post-Order Traversal (LRN): Left subtree, Right subtree, Node
def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value] if root else []

# Breadth-First Traversal (Level Order): Level by level from top to bottom and left to right within each level
def breadth_first_traversal(root):
    if not root:
        return []
    queue, result = [root], []
    while queue:
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


