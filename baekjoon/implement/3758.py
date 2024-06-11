import sys
input = sys.stdin.readline

t = int(input())


def calculate():
    return sorted(result, key=lambda x: (x[0], -x[1], -x[2]), reverse=True)


for _ in range(t):
    n, k, t, m = map(int, input().split())
    points = [[0] * k for _ in range(n)]
    result = [[0, 0, 0, i + 1] for i in range(n)]
    for time in range(m):
        i, j, s = map(int, input().split())
        if points[i - 1][j - 1] < s:
            result[i - 1][0] = result[i - 1][0] - points[i - 1][j - 1] + s
            points[i - 1][j - 1] = s
        result[i - 1][-2] = time
        result[i - 1][-3] += 1
    result = calculate()
    rank = 0
    for i in range(len(result)):
        if result[i][-1] == t:
            rank = i + 1
            break
    print(rank)
