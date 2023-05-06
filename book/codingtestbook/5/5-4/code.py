from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, str(input()))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < m:
                if arr[n_x][n_y] == 1:
                    q.append([n_x, n_y])
                    arr[n_x][n_y] += arr[x][y]
bfs()
print(arr[n-1][m-1])