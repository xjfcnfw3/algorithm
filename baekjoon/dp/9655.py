n = int(input())

dp = [-1] * n
dp[0] = 1

for i in range(1, n):
    if i - 3 < 0:
        dp[i] = 2 if dp[i - 1] == 1 else 1
    else:
        dp[i] = 2 if dp[i - 3] == 1 else 1
if dp[-1] == 1:
    print("SK")
else:
    print("CY")
