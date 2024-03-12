import sys

input = sys.stdin.readline
from collections import deque
n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, dist = map(int, input().split())
    tree[parent].append([child, dist])
    tree[child].append([parent, dist])

def bfs(node):
    q = deque()
    q.append((node, 0))
    visited = [False] * (n + 1)
    visited[node] = True
    result = [0, 0]

    while q:
        current_node, current_cost = q.popleft()
        for next_node, node_cost in tree[current_node]:
            if not visited[next_node]:
                next_cost = current_cost + node_cost
                q.append((next_node, next_cost))
                visited[next_node] = True
                if result[1] < next_cost:
                    result[0] = next_node
                    result[1] = next_cost
    return result
node, _ = bfs(1)
print(bfs(node)[1])