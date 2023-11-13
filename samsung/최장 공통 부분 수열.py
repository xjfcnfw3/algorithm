T = int(input())
for test_case in range(1, T + 1):
    a, b = input().split()
    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]
    for i in range(len(b) + 1):
        for j in range(len(a) + 1):
            if i == 0 or j == 0:
                continue
            elif b[i-1] == a[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("#{} {}".format(test_case, dp[len(b)][len(a)]))