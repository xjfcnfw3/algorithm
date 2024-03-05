INF = 1e9

def solution(N, road, K):
    answer = 0

    path = [[INF] * N for _ in range(N)]

    for i in range(N):
        path[i][i] = 0

    for r in road:
        a, b, c = r
        if c >= path[a - 1][b - 1]:
            continue
        path[a - 1][b - 1] = c
        path[b - 1][a - 1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if path[i][j] > path[i][k] + path[k][j]:
                    path[i][j] = path[i][k] + path[k][j]
    print(path)
    for i in range(N):
        if path[0][i] <= K:
            answer += 1
    return answer