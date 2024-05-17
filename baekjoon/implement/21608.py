import sys

input = sys.stdin.readline

n = int(input())
people_like = dict()
board = [[0] * n for _ in range(n)]
people_position = dict()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def get_around_position(x, y, idx):
    return x + dx[idx], y + dy[idx]


def select_positions(row):
    global n
    max_ = 0
    positions = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                continue
            temp = 0
            for k in range(4):
                nx, ny = get_around_position(i, j, k)
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in row[1:]:
                        temp += 1
            if temp > max_:
                positions = [(i, j)]
                max_ = temp
            elif max_ == temp:
                positions.append((i, j))
    return positions


def check_block(arr):
    positions = []
    max_ = 0
    for x, y in arr:
        temp = 0
        for k in range(4):
            nx, ny = get_around_position(x, y, k)
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    temp += 1
        if temp > max_:
            positions = [(x, y)]
            max_ = temp
        elif max_ == temp:
            positions.append((x, y))
    return positions


def select_last_position(arr):
    min_x = 9999
    min_y = 9999
    position = (9999, 9999)
    for x, y in arr:
        if min_x > x:
            position = (x, y)
            min_x = x
        if min_x == x and min_y > y:
            min_y = y
            position = (x, y)
    return position


def setting(row):
    arr = select_positions(row)
    arr = check_block(arr)
    position = select_last_position(arr)
    board[position[0]][position[1]] = row[0]

def get_point(temp):
    if temp == 1:
        return 1
    elif temp == 2:
        return 10
    elif temp == 3:
        return 100
    elif temp == 4:
        return 1000
    return 0

def print_result():
    result = 0
    for x in range(n):
        for y in range(n):
            temp = 0
            for k in range(4):
                nx, ny = get_around_position(x, y, k)
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] in people_like[board[x][y]]:
                        temp += 1
            result += get_point(temp)
    print(result)


for i in range(n * n):
    row = list(map(int, input().split()))
    people_like[row[0]] = row[1:]
    if i == 0:
        board[1][1] = row[0]
        people_position[row[0]] = (1, 1)
    else:
        setting(row)
print_result()