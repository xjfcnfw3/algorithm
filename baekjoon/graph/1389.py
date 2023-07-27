from collections import deque, defaultdict
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1

    while q:
        next = q.popleft()

        for i in graph[next]:
            if not visited[i]:
                visited[i] = visited[next] + 1
                q.append(i)

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result)) + 1)