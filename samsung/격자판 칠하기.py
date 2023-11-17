from collections import deque

def bfs(x, y):
    global result, a, b
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == "." and graph[cx][cy] == ".":
                    result = False
                    return
                elif graph[nx][ny] == "#" and graph[cx][cy] == "#":
                    result = False
                    return
                if graph[nx][ny] == "?":
                    if graph[cx][cy] == ".":
                        graph[nx][ny] = "#"
                    elif graph[cx][cy] == "#":
                        graph[nx][ny] = "."
                q.append((nx, ny))


T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    visited = [[False] * b for _ in range(a)]
    start = (0, 0)
    graph = []
    for i in range(a):
        arr = list(input())
        if start == (0, 0):
            for j in range(b):
                if arr[j] == "#" or arr[j] == ".":
                    start = (i, j)
                    break
        graph.append(arr)
    result = True
    bfs(start[0], start[1])
    if result:
        print("#{} possible".format(test_case))