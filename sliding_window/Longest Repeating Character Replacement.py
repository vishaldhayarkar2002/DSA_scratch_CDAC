class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26

        maxLen = 0
        maxFreq = 0
        left = 0
        right = 0

        while right < n:
            ch = s[right]

            freq[ord(ch) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(ch) - ord('A')])

            if (right - left + 1) - maxFreq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen


def characterReplacement(s, k):
    left = 0
    count = {}
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        # Add current char to window
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # If too many replacements needed, shrink
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len