import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for i in range(n + 1)]

dp[1][1] = arr[0][0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = arr[i-1][j-1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(m):
    a, b, c, d = map(int, input().split())
    print(dp[c][d] - dp[c][b - 1] - dp[a - 1][d] + dp[a-1][b-1])