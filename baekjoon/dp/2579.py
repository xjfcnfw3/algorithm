n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [[0] * 2 for _ in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp[0] = [arr[0], arr[0]]
    dp[1] = [arr[1], arr[0] + arr[1]]
    for i in range(2, n):
        dp[i][0] = max(dp[i - 2][1] + arr[i], dp[i - 2][0] + arr[i])
        dp[i][1] = dp[i - 1][0] + arr[i]
    print(max(dp[-1]))