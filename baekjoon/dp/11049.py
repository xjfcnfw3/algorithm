import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * (n + 1) for _ in range(n + 1)]

arr = [[]]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for j in range(1, n + 1):
    for i in reversed(range(1, j)):
        if j == i + 1:
            dp[i][j] = arr[i][0] * arr[j][1] * arr[i][1]
        else:
            dp[i][j] = 2 ** 31
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1])
print(dp[1][n])