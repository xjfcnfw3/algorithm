r, c, n = map(int, input().split())
board = []

for _ in range(r):
    arr = list(input())
    board.append(arr)
if n == 1:
    for row in board:
        print(''.join(row))
elif n > 1 and n % 2 == 0:
    for i in range(r):
        print('O' * c)
else:
    bombs1 = [["O"] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                bombs1[i][j] = '.'
            else:
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= i + dx < r and 0 <= j + dy < c and board[i + dx][j + dy] == 'O':
                        bombs1[i][j] = '.'
                        break
    bombs2 = [["O"] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if bombs1[i][j] == 'O':
                bombs2[i][j] = '.'
            else:
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= i + dx < r and 0 <= j + dy < c and bombs1[i + dx][j + dy] == 'O':
                        bombs2[i][j] = '.'
                        break
    if n % 4 == 3:
        for row in bombs1:
            print("".join(row))
    if n % 4 == 1:
        for row in bombs2:
            print("".join(row))