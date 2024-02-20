#When MIN plays first...
def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]
    
    if isMax:
        return max(minimax(depth + 1, nodeIndex * 2, False, scores, h),
                   minimax(depth + 1, nodeIndex * 2 + 1, False, scores, h))
    else:
        return min(minimax(depth + 1, nodeIndex * 2, True, scores, h),
                   minimax(depth + 1, nodeIndex * 2 + 1, True, scores, h))

def log2(n):
    return 0 if n == 1 else 1 + log2(n // 2)

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    n = len(scores)
    h = log2(n)
    
    # When MIN plays first, we start with the minimizing player
    optimal_value = minimax(0, 0, False, scores, h)
    print(f"The optimal value is: {optimal_value}")