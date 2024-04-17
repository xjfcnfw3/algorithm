from collections import deque

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]


def bfs(m, n, time, q):
    next_q = deque()
    while q:
        cx, cy, t = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    q.append((nx, ny, time))
                elif arr[nx][ny] == 1:
                    next_q.append((nx, ny, time + 1))
                    arr[nx][ny] = time + 2
                visited[nx][ny] = True
    return next_q


q = deque()
q.append((0, 0, 0))
visited[0][0] = True
q = bfs(m, n, 0, q)
result_time = q[0][2]
result = len(q)

while q:
    q = bfs(m, n, result_time, q)
    if len(q) == 0:
        print(result_time)
        print(result)
        break
    result_time = q[0][2]
    result = len(q)
