def check_pal(arr):
    return arr[::-1] == arr

def check_row(x, y):
    global result
    for i in reversed(range(len(graph) - y + 1)):
        if check_pal(graph[x][y: y + i]):
            result = max(result, len(graph[x][y: y + i]))
        if i < result:
            break

def check_col(x, y):
    arr = []
    for i in range(len(graph) - x):
        arr.append(graph[x + i][y])
    while arr:
        if check_pal(arr):
            result = max(result, len(arr))
        if len(arr) < result:
            break
        arr.pop()

T = 1

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(input())
    graph = [arr] + [list(input()) for _ in range(len(arr)-1)]
    result = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            check_row(i , j)
            check_col(i, j)
    print("#{} {}".format(n, result))