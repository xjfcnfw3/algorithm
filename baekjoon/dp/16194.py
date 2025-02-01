n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for j in range(1, n + 1):
    for i in reversed(range(1, j + 1)):
        if i == j:
            dp[i][j] = arr[i - 1]
        else:
            for k in range(1, j - i + 1):
                if not dp[i][j]:
                    dp[i][j] = dp[k][j - i] + arr[i - 1]
                else:
                    dp[i][j] = min(dp[i][j], dp[k][j - i] + arr[i - 1])

print(min(dp[i][-1] for i in range(1, n + 1)))