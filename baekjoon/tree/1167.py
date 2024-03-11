import sys
from collections import deque
input = sys.stdin.readline
v = int(input())

tree = [[] for _ in range(v + 1)]

for _ in range(v):
    arr = list(map(int, input().split()))
    current = arr[0]
    idx = 1
    while arr[idx] != -1:
        n, c = arr[idx], arr[idx + 1]
        tree[current].append((n, c))
        idx += 2
def bfs(node):
    q = deque()
    q.append((node, 0))
    visited = [False] * (v + 1)
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