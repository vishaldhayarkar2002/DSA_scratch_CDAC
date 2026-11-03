def lps(s, low, high):

    # Base case
    if low > high:
        return 0
    # If there is only 1 character
    if low == high:
        return 1
    # If the first and last characters match
    if s[low] == s[high]:
        return lps(s, low + 1, high - 1) + 2

    # If the first and last characters do not match
    return max(lps(s, low, high - 1), lps(s, low + 1, high))


def longestPalinSubseq(s):
    return lps(s, 0, len(s) - 1)

# or here jsut we can use the lcs IMP