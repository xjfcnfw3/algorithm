import heapq
import sys
sys.setrecursionlimit(10*9)

input = sys.stdin.readline
v, e = map(int, input().split())

visited = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
result = 0
cnt = 0

for _ in range(e):
    s, e, d = map(int, input().split())
    graph[s].append([d, e])
    graph[e].append([d, s])

q = [[0, 1]]

while q:
    if cnt == v:
        break
    d, s = heapq.heappop(q)
    if not visited[s]:
        visited[s] = True
        result += d
        cnt += 1
        for i in graph[s]:
            heapq.heappush(q, i)
print(result)
