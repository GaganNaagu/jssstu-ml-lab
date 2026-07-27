class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

def minimax(node, depth, is_maximizing):
    if depth == 0 or not node.children:
        return node.value, [node.value]

    if is_maximizing:
        best_val = float("-inf")
        best_path = []
        for child in node.children:
            val, path = minimax(child, depth - 1, False)
            if val > best_val:
                best_val = val
                best_path = [node.value] + path
        return best_val, best_path
    else:
        best_val = float("inf")
        best_path = []
        for child in node.children:
            val, path = minimax(child, depth - 1, True)
            if val < best_val:
                best_val = val
                best_path = [node.value] + path
        return best_val, best_path

game_tree = TreeNode(0, [
    TreeNode(1, [TreeNode(3), TreeNode(5)]),
    TreeNode(2, [TreeNode(2), TreeNode(9)])
])

optimal_value, optimal_path = minimax(game_tree, 2, True)

print("Optimal value:", optimal_value)
print("Optimal path:", optimal_path)