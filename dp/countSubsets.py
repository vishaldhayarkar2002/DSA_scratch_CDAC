def countSubsets(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # One way to make sum 0 (empty set)
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] += dp[s - num]
    return dp[target]