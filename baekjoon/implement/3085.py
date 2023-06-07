n = int(input())

graph = [list(input()) for _ in range(n)]

def check():
    global result
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if graph[i][j] == graph[i][j - 1]:
                cnt +=1
                result = max(cnt, result)
            else:
                cnt = 1
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j - 1][i]:
                cnt += 1
                result = max(cnt, result)
            else:
                cnt = 1
result = 0
for i in range(n):
    for j in range(n):
        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            check()
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]

        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1],  graph[i][j]
            check()
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        if result == n:
            break

print(result)
