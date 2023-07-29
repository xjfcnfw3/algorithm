from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
q = deque()
visited = [[False] * m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(m):
        if temp[j] == 2:
            q.append((i, j))
            temp[j] = 0
    arr.append(temp)

while q:
    x, y = q.popleft()
    visited[x][y] = True
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
            q.append((nx, ny))
            arr[nx][ny] = arr[x][y] + 1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            print(-1, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
