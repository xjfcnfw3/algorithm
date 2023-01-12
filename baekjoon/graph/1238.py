import sys
import heapq
from collections import defaultdict

INF = sys.maxsize
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, end):
    q = [(0, start)]
    distance = defaultdict(int)
    while q:
        dist, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = dist
            if node == end:
                return dist
            for n, t in graph[node]:
                alt = dist + t
                heapq.heappush(q, (alt, n))


result = 0
for i in range(1, n + 1):
    result = max(dijkstra(i, x) + dijkstra(x, i), result)
print(result)
