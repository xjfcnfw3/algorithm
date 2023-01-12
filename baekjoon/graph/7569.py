import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
graph = []
q = deque([])

for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
        for k in range(m):
            if arr[j][k] == 1:
                q.append([i, j, k])
    graph.append(arr)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def dfs(queue: deque):
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                queue.append([nx, ny, nz])
                graph[nx][ny][nz] = graph[x][y][z] + 1

dfs(q)
result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result, graph[i][j][k])
print(result - 1)