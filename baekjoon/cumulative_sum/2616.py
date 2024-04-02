n = int(input())
arr = list(map(int, input().split()))
board_length = int(input())

sums = [0] * (len(arr) + 1)
sums[1] = arr[0]
for i in range(2, len(sums)):
    sums[i] = sums[i - 1] + arr[i - 1]

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * board_length, n + 1):
        if i == 1:
            dp[i][j] = max(dp[i][j - 1], sums[j] - sums[j - board_length])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - board_length] + sums[j] - sums[j - board_length])

print(dp[3][n])