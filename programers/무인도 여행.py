import sys

sys.setrecursionlimit(1000000)

def dfs(x, y, maps):
    global num, visited
    visited[x][y] = True
    num += int(maps[x][y])
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X" and not visited[nx][ny]:
            dfs(nx, ny, maps)


def solution(maps):
    global visited, num
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                num = 0
                dfs(i, j, maps)
                answer.append(num)
    if answer:
        return sorted(answer)
    else:
        return [-1]