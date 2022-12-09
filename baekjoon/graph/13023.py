n, m = map(int, input().split(" "))
graph = [[] for i in range(n)]
visited = [False] * 2001
for i in range(m):
    x, y = map(int, input().split(" "))
    graph[x].append(y)
    graph[y].append(x)
answer = False


def bfs(deep, v):
    global answer
    visited[v] = True
    if deep == 4:
        answer = True
        return

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            bfs(deep + 1, i)
            visited[i] = False


for i in range(n):
    bfs(0, i)
    visited[i] = False
    if answer:
        break

bfs(0, 0)
if answer:
    print(1)
else:
    print(0)
