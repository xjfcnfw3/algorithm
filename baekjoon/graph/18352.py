import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = []


def dfs(start):
    visited[start] = True
    q = deque()
    q.append([start, 0])
    while q:
        node, deep = q.popleft()
        if node not in result and deep == k:
            result.append(node)
        for i in graph[node]:
            if not visited[i]:
                q.append([i, deep + 1])
                visited[i] = True

dfs(x)
result.sort()
if result:
    for i in result:
        print(i)
else:
    print(-1)