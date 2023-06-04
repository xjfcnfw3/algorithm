import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = []
result = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    graph.append(list(map(int, input().split())))

max_val = max(map(max, graph))

def dfs(x, y, depth, cnt):
    global result
    if result >= cnt + max_val * (4 - depth):
        return
    if depth == 4:
        result = max(cnt, result)
        return

    for i in move:
        nx, ny = x + i[0], y + i[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, cnt + graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, cnt + graph[nx][ny])
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

print(result)

