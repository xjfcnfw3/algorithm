n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]


dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            continue
        if j + 1 < n and not arr[i][j + 1]:
            dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][2]

        if i + 1 < n and not arr[i + 1][j]:
            dp[i + 1][j][1] += dp[i][j][1] + dp[i][j][2]

        if i + 1 < n and j + 1 < n and not arr[i + 1][j] and not arr[i][j + 1] and not arr[i + 1][j + 1]:
            dp[i + 1][j + 1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]

print(sum(dp[-1][-1]))

