import sys
from collections import deque
input = sys.stdin.readline

r, c, t = map(int, input().split())

board = []
m = []
dust = deque()

for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] == -1:
            m.append((i, j))
        elif row[j] > 0:
            dust.append((i, j, row[j]))
    board.append(row)

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def progress1():
    global r, c
    while dust:
        x, y, value = dust.popleft()
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                board[nx][ny] += value // 5
                count += 1
        board[x][y] -= (value // 5) * count



def progress2():
    global r, c
    temp = 0
    idx = 1
    x, y = m[0][0], 1
    while True:
        nx, ny = x + dx[idx], y + dy[idx]
        if ny == c or nx == r or ny == -1 or nx == -1:
            idx = (idx - 1) % 4
            continue
        if x == m[0][0] and y == 0:
            break
        temp, board[x][y] = board[x][y], temp
        x, y = nx, ny

    temp = 0
    idx = 1
    x, y = m[1][0], 1

    while True:
        nx, ny = x + dx[idx], y + dy[idx]
        if ny == c or nx == r or ny == -1 or nx == -1:
            idx = (idx + 1) % 4
            continue
        if x == m[1][0] and y == 0:
            break
        temp, board[x][y] = board[x][y], temp
        x, y = nx, ny

for _ in range(t):
    progress1()
    progress2()
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dust.append((i, j, board[i][j]))
print(sum(dust[i][2] for i in range(len(dust))))