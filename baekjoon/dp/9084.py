import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    dp = [[0] * (m + 1) for _ in range(len(arr))]

    for i in range(len(arr)):
        if arr[i] <= m:
            dp[i][arr[i]] = 1

    for i in range(1, m + 1):
        for j in range(len(arr)):
            if dp[j][i] > 0:
                for k in range(j, len(arr)):
                    value = arr[k]
                    if value + i <= m:
                        dp[k][value + i] += dp[j][i]
    print(sum(dp[i][-1] for i in range(len(arr))))