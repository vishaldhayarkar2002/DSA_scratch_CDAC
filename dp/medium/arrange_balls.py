
from functools import lru_cache

def countArrangements(R, G, B):

    @lru_cache(None)
    def solve(r, g, b, last):

        # All balls have been arranged successfully
        if r == 0 and g == 0 and b == 0:
            return 1

        ways = 0

        # Place red if available and previous ball isn't red
        if r > 0 and last != 0:
            ways += solve(r - 1, g, b, 0)

        # Place green if available and previous ball isn't green
        if g > 0 and last != 1:
            ways += solve(r, g - 1, b, 1)

        # Place blue if available and previous ball isn't blue
        if b > 0 and last != 2:
            ways += solve(r, g, b - 1, 2)

        return ways

    # 3 represents no previous ball
    return solve(R, G, B, 3)


print(countArrangements(2, 1, 1))
# Output: 6
