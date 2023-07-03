import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())


def bfs(n, m):
    q = deque()
    q.append((n, 1))
    while q:
        num, count = q.popleft()
        if num == m:
            print(count)
            exit(0)
        if num * 10 + 1 <= m:
            q.append((num * 10 + 1, count + 1))

        if num * 2 <= m:
            q.append((num * 2, count + 1))

bfs(n, m)
print(-1)