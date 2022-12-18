import sys

sys.setrecursionlimit(100000000)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

MAX = 10 ** 8
price = MAX


def dfs(start, current, path, visited):
    global price

    if n == len(visited):
        if graph[current][start]:
            price = min(price, path + graph[current][start])
        return
    for end in range(n):
        if graph[current][end] and end not in visited and path < price:
            visited.append(end)
            dfs(start, end, path + graph[current][end], visited)
            visited.pop()


for i in range(n):
    dfs(i, i, 0, [i])
print(price)
