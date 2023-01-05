import heapq
from collections import defaultdict
import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
start = int(input())

graph = defaultdict(list)
distance = defaultdict(int)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 함수
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

for i in range(1, n + 1):
    if i not in distance:
        print("INFINITY")
    else:
        print(distance[i])