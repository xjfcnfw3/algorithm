n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
def check(x, y):
    if x + 1 < n and graph[x + 1][y] == 0:
        return True
    elif x - 1 >= 0 and graph[x - 1][y] == 0:
        return True
    elif y + 1 < m and graph[x][y + 1] == 0:
        return True
    elif y - 1 >= 0 and graph[x][y - 1] == 0:
        return True
    return False

def move(x, y, d):
    if d == 0:
        return x - 1, y
    elif d == 1:
        return x, y + 1
    elif d == 2:
        return x + 1, y
    else:
        return x, y - 1

def move_back(x, y, d):
    if d == 0:
        return x + 1, y
    elif d == 1:
        return x, y - 1
    elif d == 2:
        return x - 1, y
    else:
        return x, y + 1

def dfs(x, y):
    global result, d
    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1
    if check(x, y):
        for _ in range(1, 5):
            d = (d - 1) % 4
            nx, ny = move(x, y, d)
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                dfs(nx, ny)
                break
    else:
        nx, ny = move_back(x, y, d)
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
            dfs(nx, ny)
        else:
            return

dfs(r, c)
print(result)