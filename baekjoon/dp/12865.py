n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n + 1)]
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = arr[i][0]
        value = arr[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])