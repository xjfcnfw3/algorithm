import sys

input = sys.stdin.readline

n = int(input())
dp = [[0] * 2 for _ in range(n)]
arr = list(map(int, input().split()))
result = arr[0]
dp[0][0], dp[0][1] = arr[0], -1e9

for i in range(1, n):
    dp[i][0]= arr[i]
    dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])
    dp[i][0] = max(dp[i - 1][0] + arr[i], dp[i][0])
    result = max(result, dp[i][0], dp[i][1])
print(result)