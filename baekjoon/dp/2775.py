dp = [[i for i in range(1, 15)]] + [[0] * 14 for _ in range(14)]

for i in range(1, 15):
    for j in range(14):
        if i == 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n - 1])