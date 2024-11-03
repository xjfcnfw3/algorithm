n = int(input())
dp = [-1] * n
arr = list(map(int, input().split()))
dp[0] = 0

for i in range(n):
    if dp[i] == -1:
        continue
    for j in range(1, arr[i] + 1):
        if i + j < n:
            if dp[i + j] == -1 or dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1
        elif i + j >= n:
            break
print(dp[-1])