import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = defaultdict(list)
distance = defaultdict(int)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = [(0, start)]
    while q:
        price, node = heapq.heappop(q)
        if node not in distance:
            distance[node] = price
            for n, t in graph[node]:
                alt = t + price
                heapq.heappush(q, (alt, n))


dijkstra(start)
print(distance[end])