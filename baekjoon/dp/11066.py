import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_arr = [0]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        sum_arr.append(sum_arr[-1] + arr[i - 1])

    for j in range(1, n + 1):
        for i in reversed(range(1, j)):
            if i == j - 1:
                dp[i][j] = arr[i] + arr[i - 1]
            else:
                for k in range(i, j):
                    if dp[i][j] == 0:
                        dp[i][j] = dp[i][k] + dp[k + 1][j] + sum_arr[j] - sum_arr[i - 1]
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum_arr[j] - sum_arr[i - 1])
    print(dp[1][n])
