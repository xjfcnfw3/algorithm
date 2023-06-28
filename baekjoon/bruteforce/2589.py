from collections import deque

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

result = 0


def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    num = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or n <= nx or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[cx][cy] + 1
                num = max(num, visited[nx][ny])
                q.append((nx, ny))
    return num - 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
