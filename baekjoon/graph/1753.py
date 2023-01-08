import heapq
from collections import defaultdict
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

graph = defaultdict(list)
distance = defaultdict(int)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = [(0, start)]
    while q:
        dist, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = dist
            for n, t in graph[node]:
                alt = dist + t
                heapq.heappush(q, (alt, n))


dijkstra(start)

for i in range(1, v + 1):
    if i not in distance:
        print("INF")
    else:
        print(distance[i])
