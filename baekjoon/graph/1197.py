import sys

input = sys.stdin.readline

arr = []
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

for i in range(e):
    arr.append(list(map(int, input().split())))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]



arr.sort(key=lambda x: x[2])
result = 0
for a, b, cost in arr:
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)
    if a_root != b_root:
        if a_root < b_root:
            parent[b_root] = a_root
        else:
            parent[a_root] = b_root
        result += cost

print(result)
