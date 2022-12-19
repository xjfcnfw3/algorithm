import sys
from collections import deque

x, y = map(int, input().split())

min_dist = sys.maxsize

obj = {}

for _ in range(x):
    a, b = map(int, input().split())
    obj[a] = b

for _ in range(y):
    a, b = map(int, input().split())
    obj[a] = b

visited = [False] * 101

def bfs():
    global min_dist
    queue = deque()
    queue.append([1, 0])
    visited[1] = True
    while queue:
        v, dist = queue.popleft()
        if v == 100:
            min_dist = min(min_dist, dist)
        for i in range(1, 7):
            next_v = i + v
            if dist < min_dist and next_v <= 100:
                if next_v in obj:
                    queue.append([obj[next_v], dist + 1])
                    visited[obj[next_v]] = True
                else:
                    if not visited[next_v]:
                        queue.append([next_v, dist + 1])
                        visited[next_v] = True


bfs()
print(min_dist)
