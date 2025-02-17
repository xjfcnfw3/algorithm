n, east, west, south, north = map(int, input().split())

graph = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

answer = 0

percent_data = [east, west, south, north]


def dfs(x, y, percent, depth):
    global answer
    if depth == n:
        answer += percent
        return

    graph[x][y] = 1

    for dx, dy, idx in ((0, 1, 0), (0, -1, 1), (1, 0, 2), (-1, 0, 3)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < (2 * n + 1) and 0 <= ny < (2 * n + 1) and not graph[nx][ny]:
            dfs(nx, ny, percent * (percent_data[idx] / 100), depth + 1)
            graph[nx][ny] = 0


dfs(n, n, 1, 0)

print(answer)
