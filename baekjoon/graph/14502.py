import copy
from collections import deque

n, m = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = []
result = 0
block = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            block += 1


def bfs():
    global result
    virus = 0
    lab = copy.deepcopy(graph)
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                virus += 1
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if lab[nx][ny] == 0:
                lab[nx][ny] = 2
                virus += 1
                q.append([nx, ny])

    cnt = 0
    for i in range(n):
        cnt += lab[i].count(0)
    result = max(result, cnt)


def make_wall(depth):
    if depth == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(depth + 1)
                graph[i][j] = 0


make_wall(0)
print(result)
