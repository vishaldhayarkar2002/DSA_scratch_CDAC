def wordBreak(s, wordDict):
    words = set(wordDict)               # O(1) lookup
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True                        # empty prefix is breakable

    for i in range(1, n + 1):
        for j in range(i):
            # If prefix s[:j] is breakable and s[j:i] is a word → s[:i] breakable
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break                   # no need to check other j
    return dp[n]

