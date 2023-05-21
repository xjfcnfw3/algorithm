from collections import deque

n, m = map(int, input().split())
graph = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]
        for i in move:
            n_x = x + i[0]
            n_y = y + i[1]
            if 0 <= n_x < n and 0 <= n_y < m:
                if not visited[n_x][n_y][wall]:
                    if graph[n_x][n_y] == 1 and wall == 0:
                        visited[n_x][n_y][1] = visited[x][y][0] + 1
                        q.append([n_x, n_y, 1])
                    elif graph[n_x][n_y] == 0:
                        q.append([n_x, n_y, wall])
                        visited[n_x][n_y][wall] = visited[x][y][wall] + 1
    return -1

result = bfs()
print(result)