def dfs_iter(graph, start):
    stack = [start]
    visited = set()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                stack.append(v)
    return visited

# recusrsive
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, u, visited):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited)