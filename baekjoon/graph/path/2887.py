import heapq, sys

input = sys.stdin.readline

n = int(input())
x = []
y = []
z = []

q = []

for i in range(n):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

for i in range(n - 1):
    heapq.heappush(q, (abs(x[i][0] - x[i + 1][0]), x[i][1], x[i + 1][1]))
    heapq.heappush(q, (abs(y[i][0] - y[i + 1][0]), y[i][1], y[i + 1][1]))
    heapq.heappush(q, (abs(z[i][0] - z[i + 1][0]), z[i][1], z[i + 1][1]))

result = 0

parent = [i for i in range(n)]


def find(num):
    if num != parent[num]:
        parent[num] = find(parent[num])
    return parent[num]


def union(a, b, v):
    global result
    a_root = find(a)
    b_root = find(b)

    if a_root > b_root:
        parent[a_root] = b_root
        result += v
    elif a_root == b_root:
        return
    else:
        parent[b_root] = a_root
        result += v


while q:
    v, a, b = heapq.heappop(q)
    union(a, b, v)
print(result)