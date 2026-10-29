from collections import deque

def bfs(graph, start):
    q = deque([start])
    res = [] # result array
    visited = {start}
    dist = {start: 0}
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                dist[v] = dist[u] + 1
                q.append(v)
    return dist