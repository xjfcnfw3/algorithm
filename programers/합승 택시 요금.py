INF = 200 * 100000
def solution(n, s, a, b, fares):
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for edge in fares:
        dist[edge[0] - 1][edge[1] - 1] = edge[2]
        dist[edge[1] - 1][edge[0] - 1] = edge[2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    answer = INF
    for i in range(n):
        answer = min(answer, dist[s - 1][i] + dist[i][a - 1] + dist[i][b - 1])
    return answer