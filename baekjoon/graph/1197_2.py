import heapq
import sys

input = sys.stdin.readline

q = []
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

result = 0
while q:
    cost, a, b = heapq.heappop(q)
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)
    if a_root != b_root:
        if a_root < b_root:
            parent[b_root] = a_root
        else:
            parent[a_root] = b_root
        result += cost

print(result)