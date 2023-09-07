from collections import defaultdict

def dfs(n, depth, visited):
    global result
    result = max(depth, result)
    for num in graph[n]:
        if num not in visited:
            dfs(num, depth + 1, visited + [num])
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = 1
    for i in range(1, n + 1):
        dfs(i, 1, [i])
    print('#{} {}'.format(test_case, result))