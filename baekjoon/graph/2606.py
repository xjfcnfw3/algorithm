from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
v = int(input())

graph = defaultdict(list)
visited = [0] * (n + 1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = -1

def dfs(x):
    global result
    result += 1
    visited[x] = 1
    for end in graph[x]:
        if not visited[end]:
            dfs(end)

dfs(1)

print(result)