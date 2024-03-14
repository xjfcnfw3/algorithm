from collections import defaultdict
import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
tree = defaultdict(list)
LOG = math.ceil(math.log2(n))

def dfs(node, d):
    depth[node] = d
    for next, cost in tree[node]:
        if depth[next] == -1:
            parent[next][0] = node
            visited[next] = visited[node] + cost
            dfs(next, d + 1)

for _ in range(n - 1):
    a, b, c = list(map(int, input().split()))
    tree[a].append((b, c))
    tree[b].append((a, c))

depth = [-1] * (n + 1)
parent = [[-1] * LOG for _ in range(n + 1)]
visited = [0] * (n + 1)

dfs(1, 0)

for i in range(1, LOG):
    for j in range(1 , n+ 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    need = depth[b] - depth[a]

    for i in range(LOG - 1, -1, -1):
        if need >= (1 << i):
            b = parent[b][i]
            need -= 1 << i
    if a == b:
        return a

    for i in range(LOG -1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

answer = []
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    answer.append(visited[a] + visited[b] - 2 * visited[lca(a, b)])
print(*answer, sep="\n")
