import sys

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
INF = 1e9
res = INF

def DFS(depth, idx):
    global res
    if depth == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += board[i][j]
                elif not visited[i] and not visited[j]:
                    b += board[i][j]
        res = min(res, abs(a - b))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1, i + 1)
            visited[i] = False

DFS(0, 0)
print(res)