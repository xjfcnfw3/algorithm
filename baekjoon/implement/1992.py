import math

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

def zip_board(x, y, n):
    num = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != num:
                num = -1
                break
    if num != -1:
        print(str(num), end="")
    else:
        print("(", end="")
        n //= 2
        zip_board(x, y, n)
        zip_board(x, y + n, n)
        zip_board(x + n, y, n)
        zip_board(x + n, y + n, n)
        print(")", end = "")

zip_board(0, 0, n)