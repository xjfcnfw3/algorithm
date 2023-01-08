import sys

INF = sys.maxsize

n = int(input())
m = int(input())

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if distance[a][b] > c:
        distance[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if distance[a][b] == INF:
            print(0, end=" ")
        else:
            print(distance[a][b], end=" ")
    print()
