import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
cycle_station = [False] * (n + 1)
graph = [[i] for i in range(n + 1)]
distance = [-1] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start, current, cnt):
    visited[current] = True
    if start == current and cnt >= 2:

        return

    visited[current] = True
    for i in graph[current]:
        if not visited[i]:
            dfs(start, i, cnt + 1)
        elif i == start and cnt >= 2:
            dfs(start, i, cnt)


def bfs():
    global distance
    q = deque()

    for i in range(1, n + 1):
        if cycle_station[i]:
            distance[i] = 0
            q.append(i)

    while q:
        node = q.popleft()
        for i in graph[node]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[node] + 1


for i in range(1, n + 1):
    dfs(i, i, 0)
    visited[i] = False

bfs()

for i in range(1, n + 1):
    print(distance[i], end=' ')