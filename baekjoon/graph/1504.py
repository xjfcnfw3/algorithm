from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, value = map(int, input().split())
    graph[a].append((value, b))
    graph[b].append((value, a))
v1, v2 = map(int, input().split())

def dijkstra(start, dist):
    q = [(0, start)]
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for c, n in graph[node]:
            alt = c + cost
            if alt < dist[n]:
                dist[n] = alt
                heapq.heappush(q, (alt, n))

dist = [INF] * (n + 1)
dijkstra(1, dist)
path_a = dist[v1]
path_b = dist[v2]

dist = [INF] * (n + 1)
dijkstra(v1, dist)
path_a += dist[v2]
path_b += dist[n]

dist = [INF] * (n + 1)
dijkstra(v2, dist)
path_a += dist[n]
path_b += dist[v1]

result = min(path_a, path_b)
print(result if result < INF else -1)
