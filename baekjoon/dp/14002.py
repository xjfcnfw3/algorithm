import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = []

for i in range(len(arr)):
    dp.append([arr[i]])

result = dp[0]

for i in range(len(arr)):
    for j in range(i):
        if arr[j] < arr[i]:
            if len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [arr[i]]
    if len(dp[i]) > len(result):
        result = dp[i]
print(len(result))
print(*result)
