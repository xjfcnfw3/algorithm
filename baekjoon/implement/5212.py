# 인접한 바다가 3칸 이상 -> 잠김
r, c = map(int, input().split())

x1, y1, x2, y2 = r, c, -1, -1

board = [['.'] * (c + 2)] + [['.'] + list(input()) + ['.'] for _ in range(r)] + [['.'] * (c + 2)]

next_sea = set()

def check(i, j):
    global r, c, x1, x2, y1, y2
    sea = 0
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx, ny = i + dx, j + dy
        if 0 <= nx <= r + 1 and 0 <= ny <= c + 1:
            if board[nx][ny] == ".":
                sea += 1
            if sea >= 3:
                next_sea.add((i, j))
                return

    x1 = min(i, x1)
    y1 = min(j, y1)
    x2 = max(i, x2)
    y2 = max(j, y2)

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if board[i][j] == "X":
            check(i, j)

for i, j in next_sea:
    board[i][j] = "."
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        print(board[i][j], end="")
    if i != x2:
        print()
