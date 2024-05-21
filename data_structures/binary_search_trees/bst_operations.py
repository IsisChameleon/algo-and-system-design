from BST import BST

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value] if root else []

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


