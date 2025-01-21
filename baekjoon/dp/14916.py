n = int(input())

dp = [-1] * (n + 1)

if n < 2:
    print(-1)
    exit(0)

dp[2] = 1

if n >= 5:
    dp[5] = 1

for i in range(1, n):
    if dp[i] == -1:
        continue
    if i + 2 <= n:
        if dp[i + 2] == -1:
            dp[i + 2] = dp[i] + 1
        else:
            dp[i + 2] = min(dp[i] + 1, dp[i + 2])
    if i + 5 <= n:
        if dp[i + 5] == -1:
            dp[i + 5] = dp[i] + 1
        else:
            dp[i + 5] = min(dp[i] + 1, dp[i + 5])
print(dp[-1])
