def check_row(x):
    s = set()
    for i in range(9):
        if arr[x][i] in s:
            return False
        s.add(arr[x][i])
    return True


def check_col(y):
    s = set()
    for i in range(9):
        if arr[i][y] in s:
            return False
        s.add(arr[i][y])
    return True


def check_box(x, y):
    s = set()
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if arr[i][j] in s:
                return False
            s.add(arr[i][j])
    return True


def check(x, y):
    global result
    if not check_row(x):
        result = False
        return
    if not check_col(y):
        result = False
        return
    if x % 3 == 0 and y % 3 == 0 and not check_box(x, y):
        result = False
        return


T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = True
    for i in range(9):
        for j in range(9):
            check(i, j)
            if not result:
                break
        if not result:
            break
    if result:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))