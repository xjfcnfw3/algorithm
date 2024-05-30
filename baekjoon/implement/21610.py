import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = {(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)}

def move(d, s):
    global n
    next = set()
    for x, y in clouds:
        x, y = (x + dx[d - 1] * s) % n, (y + dy[d - 1] * s) % n
        board[x][y] += 1
        next.add((x, y))
    return next

def check_around(x, y):
    global n
    result = 0
    for dx, dy in ((1, 1), (-1, 1), (1,- 1), (-1, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
            result += 1
    return result
def magic(next):
    for x, y in next:
        result = check_around(x, y)
        board[x][y] += result

def make_cloud(clouds):
    global n
    next_clouds = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in clouds:
                board[i][j] -= 2
                next_clouds.add((i, j))
    return next_clouds

for _ in range(m):
    d, s = map(int, input().split())
    next = move(d, s)
    clouds = next
    magic(clouds)
    clouds = make_cloud(clouds)
print(sum(sum(board[i]) for i in range(n)))