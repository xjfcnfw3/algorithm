import sys

input = sys.stdin.readline

m = []
blank = []

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if arr[j] == 0:
            blank.append((i, j))
    m.append(arr)

def search_block(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == m[nx + i][ny + j]:
                return False
    return True

def search_row(x, n):
    for i in range(9):
        if n == m[x][i]:
            return False
    return True

def search_col(y, n):
    for i in range(9):
        if n == m[i][y]:
            return False
    return True

def solution(n):
    if n == len(blank):
        for i in range(9):
            print(*m[i])
        exit(0)

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if search_row(x, i) and search_col(y, i) and search_block(x, y, i):
            m[x][y] = i
            solution(n + 1)
            m[x][y] = 0

solution(0)