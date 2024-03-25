from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        graph[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1

q = deque()
result = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    result.append(num)

    for i in graph[num]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
if len(result) != n:
    print(0)
else:
    print(*result, sep='\n')