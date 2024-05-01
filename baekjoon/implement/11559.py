from collections import deque
ROW = 12
COL = 6
board = [list(input()) for _ in range(ROW)]
answer = 0


def dfs(q, x, y, depth, color):
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROW and 0 <= ny < COL and board[nx][ny] == color and [nx, ny] not in q:
            q.append([nx, ny])
            dfs(q, nx, ny, depth + 1, color)


def move():
    while True:
        complete = True
        for i in reversed(range(1, ROW)):
            for j in range(COL):
                if board[i][j] == '.' and board[i - 1][j] != '.':
                    complete = False
                    board[i][j] = board[i - 1][j]
                    board[i - 1][j] = '.'
        if complete:
            break

def del_color(q):
    while q:
        x, y = q.popleft()
        board[x][y] = '.'

move()
while True:
    result = False
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] != '.':
                q = deque()
                q.append([i, j])
                dfs(q, i, j, 1, board[i][j])
                if len(q) >= 4:
                    del_color(q)
                    result = True
    move()
    if not result:
        break
    answer += 1
print(answer)
