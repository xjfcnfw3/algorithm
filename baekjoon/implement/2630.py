import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

def cut(x, y, n):
    global w, b
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return
    if color:
        b += 1
    else:
        w += 1

cut(0, 0, n)
print(w)
print(b)