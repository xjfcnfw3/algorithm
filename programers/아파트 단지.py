def dfs(x, y):
    global w, h, temp
    temp += 1
    visited[x][y] = True

    for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == "*" and not visited[nx][ny]:
            dfs(nx, ny)


w, h = map(int, input().split())
visited = [[False] * w for _ in range(h)]
graph = [list(input()) for _ in range(h)]
answer = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == "*" and not visited[i][j]:
            temp = 0
            dfs(i, j)
            answer = max(temp, answer)
print(answer)