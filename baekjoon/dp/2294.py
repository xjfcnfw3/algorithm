import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
dp = [-1] * (k + 1)

while dp[-1] > k:
    dp.pop()

for i in range(n):
    if arr[i] <= k:
        dp[arr[i]] = 1

for i in range(1, k + 1):
    for j in range(len(arr)):
        value = arr[j]
        if value + i > k:
            break
        elif dp[i] == -1:
            continue
        result = 1 + dp[i]
        if dp[i + value] == -1:
            dp[i + value] = result
        elif dp[i + value] > result:
            dp[i + value] = result

print(dp[-1], sep="\n")