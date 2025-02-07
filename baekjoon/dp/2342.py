arr = list(map(int, input().split()))
arr.pop()

dp = [[[1e9] * 5 for _ in range(5)] for _ in range(len(arr) + 1)]
dp[0][0][0] = 0
point = {
    0: {
        1: 2,
        2: 2,
        3: 2,
        4: 2
    },
    1: {
        1: 1,
        2: 3,
        3: 4,
        4: 3
    },
    2: {
        1: 3,
        2: 1,
        3: 3,
        4: 4
    },
    3: {
        1: 4,
        2: 3,
        3: 1,
        4: 3
    },
    4: {
        1: 3,
        2: 4,
        3: 3,
        4: 1
    }
}


for i in range(1, len(arr) + 1):
    block = arr[i - 1]
    for left in range(5):
        for right in range(5):
            if dp[i - 1][left][right] == 1e9:
                continue

            dp[i][block][right] = min(dp[i][block][right], dp[i - 1][left][right] + point[left][block])
            dp[i][left][block] = min(dp[i][left][block], dp[i - 1][left][right] + point[right][block])
result = 1e9 + 1
for i in range(5):
    for j in range(5):
        result = min(result, dp[len(arr)][i][j])

print(result)
