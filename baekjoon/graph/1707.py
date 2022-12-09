import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, color):
    global answer

    if not answer:
        return

    visited[start] = color

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -color)
        elif visited[start] == visited[i]:
            answer = False
            return


t = int(input())

for _ in range(t):
    v, e = map(int, input().split(" "))
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    answer = True

    for _ in range(e):
        x, y = map(int, input().split(" "))
        graph[x].append(y)
        graph[y].append(x)

    for j in range(1, v + 1):
        if not visited[j]:
            dfs(j, 1)

            if not answer:
                break

    if answer:
        print("YES")
    else:
        print("NO")
