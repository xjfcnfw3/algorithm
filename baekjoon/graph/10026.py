import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    color = grid[x][y]
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        X, Y = q.popleft()
        for m in move:
            n_x, n_y = X + m[0], Y + m[1]
            if 0 <= n_x < n and 0 <= n_y < n:
                if not visited[n_x][n_y] and grid[n_x][n_y] == color:
                    q.append([n_x, n_y])
                    visited[n_x][ n_y] = True

result1, result2 = 0, 0

for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            bfs(x, y)
            result1 += 1

for x in range(n):
    for y in range(n):
        if grid[x][y] == 'G':
            grid[x][y] = 'R'

visited = [[False] * n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            bfs(x, y)
            result2 += 1

print(result1, result2)
