BOARD_SIZE = 19
board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]

dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]


def check(x, y):
    for idx in range(4):
        nx, ny, depth = x, y, 1
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == board[x][y]:
            if depth == 5:
                if 0 <= nx + dx[idx] < BOARD_SIZE and 0 <= ny + dy[idx] < BOARD_SIZE and board[nx][ny] == \
                        board[nx + dx[idx]][ny + dy[idx]]:
                    break
                elif 0 <= x - dx[idx] < BOARD_SIZE and 0 <= y - dy[idx] < BOARD_SIZE and board[nx][ny] == \
                        board[x - dx[idx]][y - dy[idx]]:
                    break
                print(board[x][y])
                print(x + 1, y + 1)
                exit(0)
            nx, ny, depth = nx + dx[idx], ny + dy[idx], depth + 1


for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] == 0:
            continue
        check(i, j)
print(0)
