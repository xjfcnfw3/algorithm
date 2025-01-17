n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = arr[0][0]

for i in range(n):
    for j in range(m):
        if i == n - 1 and j == m - 1:
            break
        for dx, dy in ((1, 0), (0, 1), (1, 1)):
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                dp[nx][ny] = max(dp[nx][ny], dp[i][j] + arr[nx][ny])
print(dp[-1][-1])
