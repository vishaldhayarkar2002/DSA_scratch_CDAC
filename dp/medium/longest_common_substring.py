def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # dp[0][*] and dp[*][0] are already 0 (base case)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                best = max(best, dp[i][j]) 
            else:
                dp[i][j] = 0 # break the run (NOT max like LCS)
                # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) in case of lcs
               
    return best # that is max(dp)
    # return dp[m][n]
    
# Key mental hook: "Substring = mismatch resets to 0. Subsequence = mismatch takes max(up, left)."