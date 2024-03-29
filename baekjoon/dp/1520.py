import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
result = 0


def dfs(x, y, n, m):
    global result

    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = dx + x, dy + y
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] < graph[x][y]:
                ways += dfs(nx, ny, n, m)
    dp[x][y] = ways
    return dp[x][y]


print(dfs(0, 0, n, m))
