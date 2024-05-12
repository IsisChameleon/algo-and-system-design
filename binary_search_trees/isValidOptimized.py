from BST import BST

def isValidOptimized(tree: BST) -> bool:
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        val = node.value
        if val <= low or val >= high:
            return False
        return validate(node.left, low, val) and validate(node.right, val, high)

    return validate(tree)
