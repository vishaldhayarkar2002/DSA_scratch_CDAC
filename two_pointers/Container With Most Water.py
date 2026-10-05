class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        maxWater = (r - l) * min(height[l], height[r])
        while l < r:
            maxWater = max(maxWater, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater
