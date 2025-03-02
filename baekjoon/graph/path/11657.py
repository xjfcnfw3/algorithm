import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dist = [1e9] * (n + 1)
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def solution(start):
    dist[start] = 0

    for i in range(1, n + 1):
        for j in range(m):
            current, next, cost = edges[j][0], edges[j][1], edges[j][2]
            if dist[current] != 1e9 and dist[next] > dist[current] + cost:
                dist[next] = dist[current] + cost
                if i == n:
                    return True
    return False

negative = solution(1)

if negative:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == 1e9:
            print(-1)
        else:
            print(dist[i])