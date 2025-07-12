def minimax(depth, node_index, is_max, scores, height):
    if depth == height:                            # Leaf node
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

scores = [3, 5, 6, 9, 1, 2, 0, -1]   # Leaf scores
tree_height = 3                     # Depth of tree

best_score = minimax(0, 0, True, scores, tree_height)
print("The optimal value is:", best_score)
