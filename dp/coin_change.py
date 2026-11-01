# Minimum number of coins required to make amount t using the first i coin types.
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
# 
# space optimized
# here IN 0/1 Knapsack -- Backward
# Each element can be selected only once.

# Unbounded Knapsack   -- Forward
# Each element can be selected multiple times.
# Count the number of combinations.
def change(amount, coins):

    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:

        for i in range(coin, amount + 1):

            dp[i] += dp[i - coin]

    return dp[amount]