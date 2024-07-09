import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]
t = int(input())

for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = True
    else:
        dp[i][i + 1] = False

# 짧은 것부터 채운다.
for cnt in range(n - 2):
    for i in range(n - 2 - cnt):
        j = i + 2 + cnt
        if arr[i] == arr[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

for _ in range(t):
    a, b = map(int, input().split())
    if dp[a - 1][b - 1]:
        print(1)
    else:
        print(0)