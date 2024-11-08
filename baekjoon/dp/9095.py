for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)
    if n < 4:
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
        else:
            print(4)
        continue
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[-1])