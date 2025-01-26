n = int(input())
dp = []

for i in range(n + 1):
    dp.append([i])

for i in range(1, n + 1):
    if i * 3 <= n and (len(dp[i * 3]) > len(dp[i]) + 1 or len(dp[i * 3]) == 1):
        dp[i * 3] = dp[i] + [i * 3]
    if i * 2 <= n and (len(dp[i * 2]) > len(dp[i]) + 1 or len(dp[i * 2]) == 1):
        dp[i * 2] = dp[i] + [i * 2]
    if i + 1 <= n and (len(dp[i + 1]) > len(dp[i]) + 1 or len(dp[i + 1]) == 1):
        dp[i + 1] = dp[i] + [i + 1]

print(len(dp[-1]) - 1)
print(*sorted(dp[-1], reverse=True))