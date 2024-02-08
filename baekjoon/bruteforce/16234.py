from collections import deque
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
def bfs(x, y):
    global l, r, num, count
    q = deque()
    q.append((x, y))
    countries = deque()
    countries.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        num += board[cx][cy]
        count += 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = cx + dx, dy + cy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and l <= abs(board[cx][cy] - board[nx][ny]) <= r and not visited[nx][ny]:
                q.append((nx, ny))
                countries.append((nx, ny))
                visited[nx][ny] = True
    return countries

def check(x, y):
    if x - 1 >= 0 and l <= abs(board[x][y] - board[x - 1][y]) <= r:
        return True
    elif x + 1 < len(board) and l <= abs(board[x][y] - board[x + 1][y]) <= r:
        return True
    elif y + 1 < len(board[0]) and l <= abs(board[x][y] - board[x][y + 1]) <= r:
        return True
    elif y - 1 >= 0 and l <= abs(board[x][y] - board[x][y - 1]) <= r:
        return True
    return False

while True:
    offset = False
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if check(i, j) and not visited[i][j]:
                num = 0
                count = 0
                offset = True
                countries = bfs(i, j)
                while countries:
                    cx, cy = countries.popleft()
                    board[cx][cy] = num // count
    if not offset:
        break
    else:
        result += 1
print(result)
