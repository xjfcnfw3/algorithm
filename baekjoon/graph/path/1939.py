import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for i in range(len(graph)):
    graph[i].sort(reverse=True)

a, b = map(int, input().split())

visited = [0] * (n + 1)
q = []
heapq.heappush(q, (0, a))

while q:
    dist, now = heapq.heappop(q)
    dist = -1 * dist
    if now == b:
        print(dist)
        break

    if visited[now] > dist:
        continue

    for point, value in graph[now]:
        if dist == 0:
            visited[point] = value
            heapq.heappush(q, (-value, point))
        elif visited[point] < value and visited[point] < dist:
            visited[point] = min(dist, value)
            heapq.heappush(q, (-visited[point], point))
