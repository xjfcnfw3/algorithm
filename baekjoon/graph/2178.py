from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            print(graph[x][y])
            return
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m:
                if graph[a][b] == 1:
                    graph[a][b] = graph[x][y] + 1
                    q.append([a, b])


n, m = map(int, input().split(" "))

graph = []

for _ in range(n):
    graph.append(list(map(int, input()[:-1])))
bfs(0, 0)
