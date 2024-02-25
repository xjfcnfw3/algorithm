import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

for _ in range(m):
    a, b, c = map(int, input().split())
    if board[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
