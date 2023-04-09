import sys

sys.setrecursionlimit(100000)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
directions = ['d', 'l', 'r', 'u']


def solution(n, m, x, y, r, c, k):
    result = []
    flag = [False]

    def dfs(X, Y, deep, path):
        if flag[0] or abs(X - r) + abs(Y - c) + deep > k:
            return

        if deep == k:
            if (X, Y) == (r, c):
                result.append(path)
                flag[0] = True
            return

        for i in range(4):
            NX = X + dx[i]
            NY = Y + dy[i]
            if 0 < NX <= n and 0 < NY <= m:
                dfs(NX, NY, deep + 1, path + directions[i])

    z = k - abs(x - r) + abs(y - c)
    if z < 0 or z % 2 != 0:
        return 'impossible'

    dfs(x, y, 0, '')

    if result:
        return result[0]

    return "impossible"