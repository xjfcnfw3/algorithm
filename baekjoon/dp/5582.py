import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()

answer = 0

dp = [[0] * len(b) for _ in range(len(a))]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i][j] = 1
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i - 1][j - 1]
            if answer < dp[i][j]:
                answer = dp[i][j]

print(answer)
