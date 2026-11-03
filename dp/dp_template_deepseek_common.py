# dp[i] = True if s[:i] can be split into dictionary words
# dp[0] = True (empty string is breakable)

# For each i from 1..n:
#     For each j from 0..i-1:
#         if dp[j] is True AND s[j:i] is in dictionary:
#             dp[i] = True
#             break