import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def doing(x1, y1, x2, y2):
    temp = board[x1][y1]
    for ny in range(y1, y2):
        board[x1][ny] = board[x1][ny + 1]
    for nx in range(x1, x2):
        board[nx][y2] = board[nx + 1][y2]
    for ny in reversed(range(y1 + 1, y2 + 1)):
        board[x2][ny] = board[x2][ny - 1]
    for nx in reversed(range(x1 + 2, x2 + 1)):
        board[nx][y1] = board[nx - 1][y1]
    board[x1 + 1][y1] = temp


for _ in range(r):
    for i in range(min(n, m) // 2):
        doing(i, i, n - i - 1, m - i - 1)

for row in board:
    print(*row)
