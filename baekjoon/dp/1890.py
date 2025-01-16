n = int(input())

dp = [[0] * n for _ in range(n)]
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        point = arr[i][j]
        if 0 <= i + point < n and dp[i][j]:
            dp[i + point][j] += dp[i][j]
        if 0 <= j + point < n and dp[i][j]:
            dp[i][j + point] += dp[i][j]
print(dp[-1][-1])