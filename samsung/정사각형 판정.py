from collections import deque

T = int(input())


def check():
    global s_size
    x, y = q.popleft()
    for i in range(int(s_size)):
        for j in range(int(s_size)):
            if i == 0 and j == 0:
                continue
            c_x, c_y = q.popleft()
            if graph[x + i][y + j] != '#':
                return False
            if x + i != c_x or y + j != c_y:
                return False
    return True

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    q = deque()
    result = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "#":
                q.append([i, j])
    s_size = len(q) ** 0.5
    if s_size % 1 != 0:
        result = False
    else:
        result = check()

    if q:
        result = False
    if result:
        print("#{} yes".format(test_case))
    else:
        print("#{} no".format(test_case))