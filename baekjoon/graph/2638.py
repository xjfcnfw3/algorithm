import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))


result = 0
while True:
    offset = False
    visited = [[False] * m for _ in range(n)]
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                offset = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if offset:
        result += 1
    else:
        break

print(result)
