def champagneTower(poured, query_row, query_col):
    # Only need rows 0..query_row
    dp = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
    dp[0][0] = poured

    for i in range(query_row):           # don't need to process the last row
        for j in range(i + 1):           # columns 0..i exist in row i
            if dp[i][j] > 1.0:
                overflow = (dp[i][j] - 1.0) / 2.0
                dp[i+1][j]     += overflow
                dp[i+1][j+1]   += overflow

    return min(1.0, dp[query_row][query_col])