import math

n = int(input())

parents = [i for i in range(n + 1)]
arr = [list(map(float, input().split())) for _ in range(n)]
edges = []
answer = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = math.sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
        edges.append((dist, i, j))
edges.sort()

def find_parent(point):
    if point != parents[point]:
        parents[point] = find_parent(parents[point])
    return parents[point]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for edge in edges:
    d, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += d
print("{:.2f}".format(answer))