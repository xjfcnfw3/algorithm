dp = [[0] * 31 for _ in range(31)]


def nCr(n, r):
    if n == 1:
        return 1
    elif n == r or r == 0:
        return 1

    if dp[n][r] == 0:
        dp[n][r] = nCr(n - 1, r) + nCr(n - 1, r - 1)
    return dp[n][r]


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(nCr(m, n))
