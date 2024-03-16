n, m, r = map(int, input().split())

arr = []


def change(i, j, n, m):
    top = arr[i][j]
    left = arr[n - 1][j]
    bottom = arr[n - 1][m - 1]
    right = arr[i][m - 1]
    for x in range(n - 1, i, -1):
        arr[x][j] = arr[x - 1][j]
    for x in range(i, n - 1):
        arr[x][m - 1] = arr[x + 1][m - 1]
    for y in range(j, m - 1):
        arr[i][y] = arr[i][y + 1]
    for y in range(m - 1, j, -1):
        arr[n - 1][y] = arr[n - 1][y - 1]
    arr[i + 1][j] = top
    arr[n - 1][j + 1] = left
    arr[n - 2][m - 1] = bottom
    arr[i][m - 2] = right


cycle = (n - 1) * 2 + (m - 1) * 2
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(min(n, m) // 2):
    for _ in range(r % cycle):
        change(i, i, n - i, m - i)
    cycle -= 8

for l in arr:
    print(*l, sep=' ')
