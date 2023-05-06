from collections import deque

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    while q:
        n_x, n_y = q.popleft()
        for i in range(4):
            next_x = n_x + dx[i]
            next_y = n_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and arr[next_x][next_y] == '0':
                visited[next_x][next_y] = True
                q.append([next_x, next_y])

num = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == '0':
            num += 1
            bfs(i, j)
print(num)
