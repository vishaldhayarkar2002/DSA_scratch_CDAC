from collections import deque

def bfs(graph, start):
    q = deque([start])
    seen = {start}
    dist = {start: 0}
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                dist[v] = dist[u] + 1
                q.append(v)
    return dist