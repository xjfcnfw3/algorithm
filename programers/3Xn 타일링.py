def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n + 1, 2):
        dp[i] = (dp[i - 2] * 3 + sum(dp[2:i - 2]) * 2 + 2) % 1000000007
    return dp[-1]