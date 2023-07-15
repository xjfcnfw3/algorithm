import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dp = [0] * (n + 1)
arr = list(map(int, input().split()))


for i in range(1, n + 1):
    num = arr[i - 1]
    arr.append(num)
    if i > 0:
        dp[i] = dp[i - 1] + num
    elif i == 0:
        dp[i] = num

for i in range(m):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])