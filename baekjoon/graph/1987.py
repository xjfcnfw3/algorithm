import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]
alpha = [False] * 26
result = 1
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]

        if 0 <= nx < r and 0 <= ny < c:
            if not alpha[graph[nx][ny]]:
                alpha[graph[nx][ny]] = True
                dfs(nx, ny, cnt + 1)
                alpha[graph[nx][ny]] = False


alpha[graph[0][0]] = True
dfs(0, 0, result)
print(result)
