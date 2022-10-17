from collections import deque

n, m = map(int, input().split())
graph = [[]]
for i in range(n):
    arr = [0] + list(map(int, input()))
    graph.append(arr)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, visited):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        ax, ay = queue.popleft()
        for i in range(4):
            if 0 < ax + dx[i] <= n and 0 < ay + dy[i] <= m:
                if visited[ax + dx[i]][ay + dy[i]] is 0:
                    visited[ax + dx[i]][ay + dy[i]] = 1
                    queue.append([ax + dx[i], ay + dy[i]])


num = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 0:
            dfs(i, j, graph)
            num += 1

print(num)
