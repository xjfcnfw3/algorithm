import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
a = defaultdict(list)

for i in range(1, n + 1):
    v = int(input())
    a[v].append(i)

checked = [0 for _ in range(n + 1)]
result = []

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in a[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return

for i in range(1, n + 1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for i in result:
    print(i)
