def solve(nums):
    res = []
    path = []
    def backtrack(i):
        if i == len(nums):
            res.append(path[:])     # copy!
            return
        # choice 1
        backtrack(i + 1)
        # choice 2
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
    backtrack(0)
    return res


# def backtrack(state):
#     if goal(state):
#         record(state)
#         return
#     for choice in choices(state):
#         apply(choice)
#         backtrack(new_state)
#         undo(choice)

# Python gotcha: Always res.append(path[:]) — never res.append(path).