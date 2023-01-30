import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
arr = []
result = INF
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = arr[0][i]
    for j in range(1, n):
        dp[j][0] = arr[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = arr[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = arr[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for j in range(3):
        if j != i:
            result = min(result, dp[-1][j])


print(result)