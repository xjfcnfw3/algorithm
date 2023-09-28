def check_row(x, y):
    global n
    return graph[x][y:y + n] == graph[x][y:y + n][::-1]


def check_col(x, y):
    global n
    temp = []
    for i in range(n):
        temp.append(graph[x + i][y])
    return temp == temp[::-1]


T = 10

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(input()) for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8):
            if i <= 8 - n and check_col(i, j):
                result += 1
            if j <= 8 - n and check_row(i, j):
                result += 1

    print("#{} {}".format(test_case, result))