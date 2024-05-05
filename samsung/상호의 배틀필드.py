directions = {
    "U" : [(-1, 0),  "^"],
    "L" : [(0, -1), "<"],
    "R" : [(0, 1), ">"],
    "D" : [(1, 0), "v"]
}

tank = {
    "^": "U",
    "<": "L",
    ">": "R",
    "v": "D",
}

def move():
    global x, y, d, h, w
    nx, ny = x + directions[d][0][0], y + directions[d][0][1]
    if 0 > nx or h <= nx or 0 > ny or w <= ny:
        return
    if board[nx][ny] == ".":
        board[nx][ny] = board[x][y]
        board[x][y] = "."
        x, y = nx, ny

def shot():
    global x, y, d, h, w
    cx, cy = x + directions[d][0][0], y + directions[d][0][1]
    while 0 <= cx < h and 0 <= cy < w:
        if board[cx][cy] == "#":
            break
        elif board[cx][cy] == "*":
            board[cx][cy] = "."
            break
        cx, cy = cx + directions[d][0][0], cy + directions[d][0][1]

T = int(input())
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    x, y, d = 0, 0, "U"
    board = []
    for i in range(h):
        row = list(input())
        for j in range(w):
            if row[j] == "^" or  row[j] == "<" or row[j] == ">" or row[j] == "v":
                x, y, d = i, j, tank[row[j]]
        board.append(row)
    n = int(input())
    arr = list(input())
    for c in arr:
        if c != "S":
            d = c
            board[x][y] = directions[c][1]
            move()
        else:
            shot()
    print("#{} ".format(test_case), end = "")
    for i in range(h):
        print("".join(board[i]))