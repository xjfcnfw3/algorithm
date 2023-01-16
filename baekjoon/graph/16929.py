import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split(" "))
graph = []
visited = [[False] * m for _ in range(n)]


def dfs(x, y, p_x, p_y, color):
    global answer
    visited[x][y] = True

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if 0 <= a < n and 0 <= b < m:
            if graph[a][b] == color:
                if not visited[a][b]:
                    dfs(a, b, x, y, color)
                else:
                    if a != p_x or b != p_y:
                        answer = True


for _ in range(n):
    graph.append(list(input()[:-1]))

answer = False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, i, j, graph[i][j])

if answer:
    print("Yes")
else:
    print("No")
