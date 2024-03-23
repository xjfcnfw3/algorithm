import heapq, sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
q = deque()
visited = [[0] * n for _ in range(n)]


def bfs(q, n, s):
    while q:
        cx, cy, t = q.popleft()
        if t > s:
            continue
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[cx][cy]
                    visited[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))
                elif visited[nx][ny] == t + 1 and arr[cx][cy] < arr[nx][ny]:
                    arr[nx][ny] = arr[cx][cy]
                    visited[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))
                elif visited[nx][ny] > t + 1:
                    arr[nx][ny] = arr[cx][cy]
                    visited[nx][ny] = t + 1
                    q.append((nx, ny, t + 1))


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] > 0:
            q.append((i, j, 1))
            visited[i][j] = 1
    arr.append(row)
s, x, y = map(int, input().split())
bfs(q, n, s)
print(arr[x - 1][y - 1])
