from BST import BST

def isValidOptimized(tree: BST) -> bool:

    def validate(node, lower_bound_for_node=float('-inf'), higher_bound_for_node=float('inf')):
        if not node:
            return True
        val = node.value
        if val <= lower_bound_for_node or val >= higher_bound_for_node:
            return False
        return validate(node.left, lower_bound_for_node, val) and validate(node.right, val, higher_bound_for_node)

    return validate(tree)
