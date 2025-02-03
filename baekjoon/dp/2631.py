n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [1] * n
result = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] > result:
        result = dp[i]

print(n - result)