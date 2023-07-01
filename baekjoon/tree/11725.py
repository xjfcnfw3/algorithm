import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]


def dfs(node):
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            dfs(i)

for _ in range(n - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
