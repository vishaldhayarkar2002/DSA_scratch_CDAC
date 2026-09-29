def longestConsecutive(nums):
    if not nums:
        return 0

    # Set for O(1) existence checks
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            length = 1
            current = num

            # Expand forward
            while current + 1 in num_set:
                current += 1
                length += 1

            # Update maximum
            longest = max(longest, length)

    return longest