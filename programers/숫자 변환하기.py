from collections import deque

def bfs(x, y, n):
    global answer
    visited = [False] * ((y + 1) * 2)
    q = deque()
    q.append((x, 0))

    while q:
        cx, num = q.popleft()
        if cx == y:
            answer = min(answer, num)
            continue
        if num + 1 > answer:
            continue
        if cx * 3 <= y and not visited[cx * 3]:
            visited[cx * 3] = True
            q.append((cx * 3, num + 1))
        if cx * 2 <= y and not visited[cx * 2]:
            visited[cx * 2] = True
            q.append((cx * 2, num + 1))
        if cx + n <= y and not visited[cx + n]:
            visited[cx + n] = True
            q.append((cx + n, num + 1))


def solution(x, y, n):
    global answer
    answer = 1e9
    bfs(x, y, n)
    return answer if answer != 1e9 else -1