from collections import deque

t = int(input())


def burn():
    while fires:
        cx, cy, time = fires.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = dx + cx, dy + cy
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                continue
            if graph[nx][ny] != "#":
                if visited[nx][ny] > time + 1:
                    visited[nx][ny] = time + 1
                    fires.append((nx, ny, time + 1))


def move(sx, sy):
    global x, y
    q = deque()
    q.append((sx, sy, 1))
    while q:
        cx, cy, count = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = dx + cx, dy + cy
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                print(count)
                return
            if graph[nx][ny] == "#" or graph[nx][ny] == "@" or graph[nx][ny] == "*":
                continue
            if visited[nx][ny] <= count + 1:
                continue
            if graph[nx][ny] == ".":
                graph[nx][ny] = "@"
                q.append((nx, ny, count + 1))
    print("IMPOSSIBLE")


for _ in range(t):
    y, x = map(int, input().split())
    fires = deque()
    graph = []
    offset = False
    visited = [[1e9] * y for _ in range(x)]
    start = []
    for i in range(x):
        arr = list(input())
        for j in range(len(arr)):
            if arr[j] == "*":
                fires.append((i, j, 1))
                visited[i][j] = 1
            elif arr[j] == "@":
                start = [i, j]
        graph.append(arr)
    burn()
    move(start[0], start[1])
