import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
edges = []
answer = 0
furthest = 0


def find_parents(point):
    if point != parents[point]:
        parents[point] = find_parents(parents[point])
    return parents[point]


for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

for edge in edges:
    dist, a, b = edge
    root_a = find_parents(a)
    root_b = find_parents(b)

    if root_b != root_a:
        if root_b > root_a:
            parents[root_b] = root_a
        else:
            parents[root_a] = root_b
        answer += dist
        furthest = dist
print(answer - furthest)