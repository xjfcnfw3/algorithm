from collections import deque

def bfs():
    global n
    q = deque()
    q.append((0, 0))
    dp[0][0] = graph[0][0]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] or dp[x][y] + graph[nx][ny] < dp[nx][ny]:
                    visited[nx][ny] = True
                    dp[nx][ny] = dp[x][y] + graph[nx][ny]
                    q.append((nx, ny))

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, list(input()))) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    bfs()
    print("#{} {}".format(test_case, dp[n - 1][n - 1]))