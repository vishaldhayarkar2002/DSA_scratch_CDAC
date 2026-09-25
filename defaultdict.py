# 20. What you actually need to remember for DSA

# Don't memorize every feature.

# Master these:

# 1. Grouping
from collections import defaultdict

groups = defaultdict(list)

groups[key].append(value)
# 2. Graph
graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
# 3. Counting
freq = defaultdict(int)

for x in arr:
    freq[x] += 1
# 4. Unique grouping
groups = defaultdict(set)

groups[key].add(value)
# 5. Position mapping
positions = defaultdict(list)

for i, x in enumerate(arr):
    positions[x].append(i)