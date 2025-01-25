import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            continue

        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

        result = max(dp[i][j], result)


print(result * result)