import sys

input = sys.stdin.readline

n = int(input())
arr = []
dp = [0] * (n + 1)

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n + 1):
    day, value = arr[i - 1]
    dp[i] = max(dp[i], dp[i - 1])
    fin = day + i - 1
    if fin <= n:
        dp[fin] = max(dp[i - 1] + value, dp[fin])
print(max(dp))