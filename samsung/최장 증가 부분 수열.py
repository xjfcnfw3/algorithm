T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    print("#{} {}".format(test_case, max(dp)))