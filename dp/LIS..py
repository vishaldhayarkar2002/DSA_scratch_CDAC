def lengthOfLIS(nums):
    if not nums: return 0
    dp = [1] * len(nums)  # Base: each element alone is a subseq of length 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)