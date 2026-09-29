def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n

    # Pass 1: output[i] = product of all elements to the left of i
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Pass 2: multiply by product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output