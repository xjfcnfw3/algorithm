T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(k + 1):
            w, v = arr[i]
            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
    print("#{} {}".format(test_case, dp[-1][-1]))