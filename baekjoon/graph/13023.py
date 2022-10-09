from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    start, end = map(int,input().split())
    arr[start].append(end)

checked = [0 for i in range(n)]
bfs(arr, 0, checked)
print(checked)

