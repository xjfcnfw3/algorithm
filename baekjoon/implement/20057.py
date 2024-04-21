n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

LEFT, DOWN, RIGHT, UP = 0, 1, 2, 3

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x, y = n // 2, n // 2
direction = 0
answer = 0
speed = 0
count = 0
offset = True

def wind(x, y, d):
    global answer
    if y < 0:
        return
    if d == LEFT:
        radio = left
    elif d == RIGHT:
        radio = right
    elif d == UP:
        radio = up
    else:
        radio = down
    total = 0
    for dx, dy, r in radio:
        nx, ny = x + dx, y + dy
        if r == 0:
            new_sand = board[x][y] - total
        else:
            new_sand = int(board[x][y] * r)
            total += new_sand
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += new_sand
        else:
            answer += new_sand

for i in range(2 * n - 1):
    direction = i % 4
    if direction == LEFT or direction == RIGHT:
        speed += 1
    for _ in range(speed):
        x = x + dx[direction]
        y = y + dy[direction]
        wind(x, y, direction)
print(answer)