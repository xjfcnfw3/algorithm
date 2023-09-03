import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = []
target = []

for i in range(n):
    arr = list(input().rstrip())
    for j in range(len(arr)):
        if arr[j] == "I":
            target = [i, j]
    board.append(arr)
visited = [[0] * m for _ in range(n)]

cnt = 0
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    if board[x][y] == 'P':
        cnt += 1
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if board[nx][ny] != 'X':
                dfs(nx, ny)

dfs(target[0], target[1])
if not cnt:
    print("TT")
else:
    print(cnt)