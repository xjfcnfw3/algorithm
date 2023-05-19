import heapq
from collections import defaultdict
import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)
dist = [[INF] * (k + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dijkstra():
    q = []
    count = 0
    heapq.heappush(q, (0, 1, count))

    while q:
        distance, node, c = heapq.heappop(q)
        if dist[node][c] < distance:
            continue
        for other_node, value in graph[node]:
            next_d = distance + value
            if dist[other_node][c] > next_d:
                dist[other_node][c] = next_d
                heapq.heappush(q, (next_d, other_node, c))

            if c < k and dist[other_node][c + 1] > distance:
                dist[other_node][c + 1] = distance
                heapq.heappush(q, (distance, other_node, c + 1))

dijkstra()
print(min(dist[n]))