import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = arr[0][0]

for i in range(1, m):
    dp[0][i] = arr[0][i] + dp[0][i - 1]

for i in range(1, n):
    left = [0] * m
    right = [0] * m

    for j in range(m):

        if j == 0:
            left[j] = arr[i][j] + dp[i - 1][j]
            right[m - 1 - j] = arr[i][m - 1 - j] + dp[i - 1][m - 1 - j]
            continue

        left[j] = arr[i][j] + max(left[j - 1], dp[i - 1][j])
        right[m - 1 - j] = arr[i][m - 1 - j] + max(dp[i - 1][m - 1 - j], right[m - j])

    for k in range(m):
        dp[i][k] = max(left[k], right[k])

print(dp[-1][-1])

