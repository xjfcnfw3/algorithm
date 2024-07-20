import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[1e9] * n for _ in range(n)]
path = [[-1] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)
    path[a - 1][b - 1] = a - 1


for k in range(n):
    graph[k][k] = 0
    path[k][k] = -1
    for i in range(n):
        for j in range(n):
            distance = graph[i][k] + graph[k][j]
            if graph[i][j] > distance:
                graph[i][j] = distance
                path[i][j] = path[k][j]
for i in range(n):
    for j in range(n):
        print(graph[i][j] if graph[i][j] != 1e9 else 0, end=" ")
    print()

for i in range(n):
    for j in range(n):
        if path[i][j] == -1:
            print(0)
            continue

        v = j
        ans = []
        while True:
            if v == i:
                break
            ans.append(v + 1)
            v = path[i][v]
        print(len(ans) + 1, i + 1, *ans[::-1])