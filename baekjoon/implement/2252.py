import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
degree = [0 for _ in range(n + 1)]
q = deque()
answer = []

for i in range(m):
    a, b, = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    answer.append(num)
    for i in graph[num]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*answer)