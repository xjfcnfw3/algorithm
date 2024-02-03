n, m, x, y, k = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
    x += dx[command - 1]
    y += dy[command - 1]
    if x < 0 or y < 0 or x >= n or y >= m:
        x -= dx[command - 1]
        y -= dy[command - 1]
        continue

    turn(command)

    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0
    print(dice[0])