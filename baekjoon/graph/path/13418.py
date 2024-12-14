import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m + 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [False] * (n + 1)
result = [0] * (n + 1)
q = []

visited[0] = True
max_result = 0
for b, c in graph[0]:
    heapq.heappush(q, (c, b))


while q:
    c, b = heapq.heappop(q)
    if not visited[b]:
        if c == 0:
            max_result += 1
        visited[b] = True
    else:
        continue
    for x, y in graph[b]:
        if not visited[x]:
            heapq.heappush(q, (y, x))

visited = [False] * (n + 1)
result = [0] * (n + 1)
q = []

visited[0] = True
min_result = 0
for b, c in graph[0]:
    heapq.heappush(q, (-c, b))

while q:
    c, b = heapq.heappop(q)
    if not visited[b]:
        if c == 0:
            min_result += 1
        visited[b] = True
    else:
        continue
    for x, y in graph[b]:
        if not visited[x]:
            heapq.heappush(q, (-y, x))

print(max_result**2 - min_result**2)