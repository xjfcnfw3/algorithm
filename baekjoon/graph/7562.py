from collections import deque
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    global status
    num = 0
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_d and y == y_d:
            print(visited[x][y] - 1)
            return
        for i in range(8):
            x_c = x + dx[i]
            y_c = y + dy[i]
            if 0 <= x_c < l and 0 <= y_c < l and visited[x_c][y_c] == 0:
                q.append([x_c, y_c])
                visited[x_c][y_c] = visited[x][y] + 1


t = int(input())

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split(" "))
    x_d, y_d = map(int, input().split(" "))
    visited = [[0] * l for _ in range(l)]
    answer = bfs(x, y)