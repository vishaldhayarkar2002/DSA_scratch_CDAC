# Counter = specialized dictionary for counting.

# arrays
b = a       # same list ❌
b = a[:]    # copy ✅
b = a.copy() # copy ✅

# strings
'ell' in s     # True — O(n) substring search

s.strip()      # remove whitespace both ends
s.split()      # ['hello'] — split on whitespace
"a,b,c".split(",")   # ['a', 'b', 'c']
"-".join(["a","b"])  # 'a-b'

s.find('l')    # 2  (or -1 if not found)
s.index('l')   # 2  (raises ValueError if missing)
s.startswith('he')   # True
s.endswith('lo')     # True
s.replace('l', 'L')  # 'heLLo'  (new string)

ord('a')       # 97
chr(97)        # 'a'

# Efficient string building
# BAD — O(n²) because strings are immutable
res = ""
for c in s:
    res += c.upper()

# GOOD — O(n), join once
parts = []
for c in s:
    parts.append(c.upper())
res = "".join(parts)

# Comparing s == t is O(n)	Don't assume O(1)
# s in t is O(n·m) worst case	Not free

# Topic 3 — Dict, Set, Counter, defaultdict
# dict = hash map (C++ unordered_map). Keys must be hashable (immutable: int, str, tuple — not list/dict/set).

# set = hash set (C++ unordered_set). O(1) average lookup.
# Counter = dict subclass for counting.

# defaultdict = dict that auto-creates missing keys.

d = {}
d = {"a": 1, "b": 2}

d["a"]              # 1
d["c"]              # KeyError
d.get("c")          # None
d.get("c", 0)       # 0

d["c"] = 3          # insert / update
del d["a"]          # remove
"a" in d            # O(1)
len(d)              # size

d.keys()            # view of keys
d.values()          # view of values
d.items()           # view of (key, value) pairs

for k, v in d.items():
    ...

    s = set()
s = {1, 2, 3}

s.add(4)
s.remove(4)         # KeyError if missing
s.discard(4)        # silent if missing
2 in s              # O(1)
len(s)

a | b               # union
a & b               # intersection
a - b               # difference
a ^ b               # symmetric difference


from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Important pattern
freq = Counter(s)

for x in s:
    if freq[x] == 1:
        ...

# You'll see this pattern frequently
# Find the first character that occurs only once.
from collections import Counter

s = "aabbcdde"

freq = Counter(s)

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

# 15. Finding the most frequent element
freq = Counter([1, 2, 2, 3, 3, 3])

element, count = freq.most_common(1)[0]

print(element)
print(count)

# 17. Counter with words
sentence = "apple banana apple orange banana apple"

words = sentence.split()

freq = Counter(words)

print(freq)

# Result:

# Counter({
#     'apple': 3,
#     'banana': 2,
#     'orange': 1
# })

# Pattern 5 — Top K frequent
freq.most_common(k)
c.most_common()     # sorted by count desc


from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word)) #imp 
    groups[key].append(word)


arr = [10, 20, 10, 30, 10]

positions = defaultdict(list)

for i, x in enumerate(arr):
    positions[x].append(i)
# Result: this is very useful dsa pattern

# 10 → [0, 2, 4]
# 20 → [1]
# 30 → [3]


# Next topics Topic 4 — Tuples, Unpacking, Sorting with key

# sort a list of tuples by 2nd element, then 1st
pairs = [(1, 3), (2, 1), (3, 1), (1, 2)]
sorted(pairs, key=lambda p: (p[1], p[0]))
# [(2, 1), (3, 1), (1, 2), (1, 3)]

# operator.itemgetter — faster than lambda
from operator import itemgetter
sorted(pairs, key=itemgetter(1, 0))       # same as above

from collections import Counter
# Top k frequent words (multi-key sort)
def top_k_words(words, k):
    c = Counter(words)
    # sort by count desc, then word asc
    items = sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))
    return [w for w, _ in items[:k]]

# Topic 5 — Comprehensions, enumerate, zip, Built-ins

# Generator expression (lazy — no list built)

sum(x*x for x in range(10))            # no intermediate list
any(x < 0 for x in nums)
all(x > 0 for x in nums)
max(x for x in nums if x % 2 == 0)

for i, x in enumerate(nums):
    ...
for i, x in enumerate(nums, start=1):  # 1-indexed
    ...


# zip
a = [1, 2, 3]
b = ['x', 'y', 'z']
list(zip(a, b))            # [(1,'x'), (2,'y'), (3,'z')]

for x, y in zip(a, b):
    ...

# unzip (transpose)
pairs = [(1, 'a'), (2, 'b')]
nums, chars = zip(*pairs)   # (1,2), ('a','b')



# 5. When NOT to use comprehensions
# Hot loops in competitive programming — a plain for loop is sometimes faster than a comprehension with a complex expression.

# When it hurts readability — a 3-line loop beats a 120-char nested comprehension.

# When you need to mutate in place — comprehensions build new lists.

# When you need early exit — any/all short-circuit, but a for loop with break is clearer.






# Topic 7 — Mutability, References, is vs ==, Falsy Values
# ALIAS — same object
a = [1, 2, 3]
b = a
b[0] = 99
print(a)        # [99, 2, 3]

# SHALLOW COPY — new outer list, shared inner objects
a = [[1, 2], [3, 4]]
b = a.copy()        # or a[:] or list(a)
b[0][0] = 99
print(a)            # [[99, 2], [3, 4]]  ← inner list shared!

# DEEP COPY — fully independent
import copy
b = copy.deepcopy(a)
b[0][0] = 99
print(a)            # [[1, 2], [3, 4]]  ← unchanged


# In DSA, use is only for: imp
if x is None: ...
if x is not None: ...

x = 0
if x:                 # False — 0 is falsy
    ...
if x is not None:     # True — 0 is a valid value
    ...


    # Bug 3 — Default mutable argument

def f(x, arr=[]):
    arr.append(x)
    return arr

print(f(1))   # [1]
print(f(2))   # [1, 2]  ← arr persists across calls!

# Fix: 
def f(x, arr=None): 
    if arr is None: arr = []

# copy
b = a[:]              # shallow list copy
b = a.copy()          # same
b = list(a)           # same
b = [row[:] for row in a]   # 2D deep-ish copy
import copy
b = copy.deepcopy(a)  # full deep copy

# None checks
if x is None: ...
if x is not None: ...

# empty checks
if not nums: ...
if nums: ...

# don't mutate while iterating
for x in nums[:]: ...
nums = [x for x in nums if condition]

# default arg
def f(x, arr=None):
    if arr is None:
        arr = []
    ...

# append a copy
res.append(path[:])

# correct 2D grid
grid = [[0] * m for _ in range(n)]