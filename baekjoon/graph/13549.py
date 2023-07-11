import sys
from collections import deque
a, b = map(int, input().split())

def bfs():
    result = sys.maxsize
    q = deque()
    q.append([a, 0])
    visited = [0] * 100001

    while q:
        position, count = q.popleft()
        visited[position] = True
        if position == b:
            result = min(result, count)

        if 0 <= position * 2 <= 100000 and not visited[position * 2]:
            q.append([position * 2, count])

        if 0 <= position - 1 <= 100000 and not visited[position - 1]:
            q.append([position - 1, count + 1])

        if 0 <= position + 1 <= 100000 and not visited[position + 1]:
            q.append([position + 1, count + 1])
    print(result)

bfs()