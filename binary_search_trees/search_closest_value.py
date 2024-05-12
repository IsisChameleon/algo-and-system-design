from BST import BST

def findClosestValueInBst(tree: BST, target):
    # Write your code here.
    node = tree
    best_diff_tuple = (tree, abs(target - tree.value))
    closestValue = findClosestValue(node, target, best_diff_tuple)
    return closestValue

def findClosestValue(node, target, best_diff_tuple):
    if target == node.value:
        return target
    diff = abs(node.value - target)  
    if diff < best_diff_tuple[1]:
        best_diff_tuple =(node, diff)
    if target > node.value and node.right is not None:
        return findClosestValue(node.right, target, best_diff_tuple)
    elif target < node.value and node.left is not None:
        return findClosestValue(node.left, target, best_diff_tuple)
    else:
        return best_diff_tuple[0].value