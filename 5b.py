import math

MAX, MIN = 1000, -1000

def alpha_beta_minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, h):
    if depth == h:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        for i in range(2):
            val = alpha_beta_minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, h)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(2):
            val = alpha_beta_minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, h)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
h = int(math.log(len(values), 2))

optimal_value = alpha_beta_minimax(0, 0, True, values, MIN, MAX, h)
print("The optimal value is:", optimal_value)
