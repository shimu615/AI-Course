def alpha_beta(depth, node_index, alpha, beta, is_max, scores, height):
    if depth == height:  # Leaf node
        return scores[node_index]

    if is_max:
        max_val = float('-inf')
        for i in range(2):  # 2 children (binary tree)
            val = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta, False, scores, height)
            max_val = max(max_val, val)
            alpha = max(alpha, max_val)
            if beta <= alpha:  # Pruning
                break
        return max_val
    else:
        min_val = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, alpha, beta, True, scores, height)
            min_val = min(min_val, val)
            beta = min(beta, min_val)
            if beta <= alpha:  # Pruning
                break
        return min_val

scores = [3, 5, 6, 9, 1, 2, 0, -1]
tree_height = 3

alpha = float('-inf')
beta = float('inf')

best_score = alpha_beta(0, 0, alpha, beta, True, scores, tree_height)
print("The optimal value with Alpha-Beta Pruning is:", best_score)
