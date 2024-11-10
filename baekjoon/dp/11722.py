n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n


for i in range(n):
    dp[i] = 1
    for j in range(i + 1):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))