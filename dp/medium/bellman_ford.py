def bellman_ford(V, edges, source):
    # edges = [(u, v, w), ...]
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # One more pass to detect negative cycle
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None                       # negative cycle reachable from source

    return dist


# Example
V = 5
edges = [
    (0, 1, -1), (0, 2, 4),
    (1, 2, 3), (1, 3, 2), (1, 4, 2),
    (3, 2, 5), (3, 1, 1), (4, 3, -3)
]
print(bellman_ford(V, edges, 0))   # [0, -1, 2, -2, 1]