def dfs(x, y, depth, dx, dy):
    global result
    if depth == 5:
        result = True
        return
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "o":
        dfs(nx, ny, depth + 1, dx, dy)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    result = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "o":
                for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)):
                    dfs(i, j, 1, dx, dy)
            if result:
                break
        if result:
            break
    print("#{}".format(test_case), end=" ")
    if result:
        print("YES")
    else:
        print("NO")
