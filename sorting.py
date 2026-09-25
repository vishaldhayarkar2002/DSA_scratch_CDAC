nums.sort()                                  # in-place
sorted(nums)                                 # new list
nums.sort(reverse=True)
items.sort(key=lambda x: x[1])               # by 2nd element
items.sort(key=lambda x: (-x[0], x[1]))      # primary desc, secondary asc IMP

from operator import itemgetter
items.sort(key=itemgetter(1, 0))