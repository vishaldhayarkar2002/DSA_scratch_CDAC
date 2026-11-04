def maxSquare(matrix):
    if not matrix or not matrix[0]: return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    best = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    # First row or column → max square side is just 1
                    dp[i][j] = 1
                else:
                    # Limited by the smallest of up, left, diagonal
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                best = max(best, dp[i][j])
            # else: dp[i][j] = 0 (no square ending here)

    return best


matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]
print(maxSquare(matrix))   # 3