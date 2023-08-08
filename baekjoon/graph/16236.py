import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
position = []
count = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    if 9 in arr:
        position = [i, arr.index(9)]


def bfs(x, y):
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x, y))
    result = []
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[x][y] > graph[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = visited[cx][cy] + 1
                    result.append((visited[nx][ny] - 1, nx, ny))
                elif graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append((nx, ny))
    return sorted(result, key=lambda x: (x[0], x[1], x[2]))

size = [2, 0]

while True:
    graph[position[0]][position[1]] = size[0]
    result = deque(bfs(position[0], position[1]))

    if not result:
        break
    step, x, y = result.popleft()
    count += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    graph[position[0]][position[1]] = 0
    position = [x, y]

print(count)