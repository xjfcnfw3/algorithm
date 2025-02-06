n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
result = 0


def check(x, y):
    return a[x][y] == b[x][y]

def change(x, y):
    for dx in range(3):
        for dy in range(3):
            a[x + dx][y + dy] = 1 - a[x + dx][y + dy]

if (n < 3 or m < 3) and a != b:
    print(-1)
    exit(0)

for i in range(n - 2):
    for j in range(m - 2):
        if not check(i, j):
            result += 1
            change(i, j)

if a != b:
    print(-1)
else:
    print(result)
