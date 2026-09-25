# raise recursion limit
import sys
sys.setrecursionlimit(10**6)

# memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, j):
    ...

# clear cache
dp.cache_clear()

# nested recursive helper
def solve(nums):
    @lru_cache(maxsize=None)
    def dfs(i, state):
        ...
    return dfs(0, initial_state)

# backtracking template
res = []
path = []
def backtrack(i):
    if done(i):
        res.append(path[:])       # copy!
        return
    for choice in choices(i):
        path.append(choice)
        backtrack(i + 1)
        path.pop()

# convert list to tuple for caching
@lru_cache(maxsize=None)
def dfs(state_tuple):
    ...
# call with dfs(tuple(nums))



# Sorting