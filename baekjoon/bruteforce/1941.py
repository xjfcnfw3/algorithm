from collections import deque
import sys

input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(5)]
answer = set()


def check(path):
    s_count = 0
    for x, y in path:
        if arr[x][y] == "S":
            s_count += 1
    return s_count >= 4


def bfs():
    global answer
    q = deque()

    for i in range(5):
        for j in range(5):
            q.append([(i, j)])

    while q:
        path = q.popleft()
        if len(path) == 7:
            if check(path):
                answer.add(tuple(sorted(path)))
            continue
        for cx, cy in path:
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in path:
                    q.append(path + [(nx, ny)])


bfs()
print(len(answer))
