class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

def alpha_beta(node, depth, alpha, beta, is_maximizing):
    if depth == 0 or not node.children:
        return node.value, [node.value]

    if is_maximizing:
        best_val = float("-inf")
        best_path = []
        for child in node.children:
            val, path = alpha_beta(child, depth - 1, alpha, beta, False)
            if val > best_val:
                best_val = val
                best_path = [node.value] + path
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val, best_path
    else:
        best_val = float("inf")
        best_path = []
        for child in node.children:
            val, path = alpha_beta(child, depth - 1, alpha, beta, True)
            if val < best_val:
                best_val = val
                best_path = [node.value] + path
            beta = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val, best_path

game_tree = TreeNode(0, [
    TreeNode(1, [
        TreeNode(3, [TreeNode(3), TreeNode(5)]),
        TreeNode(4, [TreeNode(6), TreeNode(9)])
    ]),
    TreeNode(2, [
        TreeNode(5, [TreeNode(1), TreeNode(2)]),
        TreeNode(6, [TreeNode(0), TreeNode(-1)])
    ])
])

optimal_value, optimal_path = alpha_beta(game_tree, 3, float('-inf'), float('inf'), True)
print("The optimal value is:", optimal_value)
print("The optimal path taken is:", optimal_path)