import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(list)
distance = defaultdict(int)
path = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = [(0, start, [start])]

    while q:
        time, node, p = heapq.heappop(q)
        if node not in distance:
            distance[node] = time
            path[node] = p
            for n, t in graph[node]:
                alt = time + t
                alt_p = p[:]
                alt_p.append(n)
                heapq.heappush(q, (alt, n, alt_p))


dijkstra(start)
print(distance[end])
print(len(path[end]))
print(*path[end])