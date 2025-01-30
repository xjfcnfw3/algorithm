import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
result = 1

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    if dp[i] > result:
        result = dp[i]

print(result)