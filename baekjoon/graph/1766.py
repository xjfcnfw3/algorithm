import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = []
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    num = heapq.heappop(q)
    result.append(num)

    for i in graph[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)
print(*result, sep=' ')