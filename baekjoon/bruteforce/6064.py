from sys import stdin


def num(m, n, x, y):
    while x <= m * n:
        if x % n == y % n:
            print(x)
            return
        x += m
    print(-1)


t = int(input())

for i in range(t):
    m, n, x, y = map(int, stdin.readline().split())
    num(m, n, x, y)
