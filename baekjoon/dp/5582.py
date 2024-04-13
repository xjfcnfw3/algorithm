import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()

answer = 0

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if answer < dp[i][j]:
                answer = dp[i][j]

print(answer)