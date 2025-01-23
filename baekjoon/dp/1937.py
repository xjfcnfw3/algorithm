import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
dp = [[0] * n for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] > arr[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            dfs(i, j)

result = 0

for i in range(n):
    result = max(result, max(dp[i]))


print(result)