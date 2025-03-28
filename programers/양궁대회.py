def get_result(a, b):
    for i in reversed(range(len(a))):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return False


def get_point(info, result):
    point = 0
    for i in range(len(info)):
        if info[i] >= result[i]:
            if info[i] == 0:
                continue
            point -= 10 - i
        else:
            point += 10 - i
    return point


def dfs(info, index, rest, arr):
    global answer, point

    if not rest or index == 11:
        if rest:
            arr = arr[:]
            arr[-1] = rest
        result = get_point(info, arr)
        if point < result:
            point = result
            answer = arr
        elif point == result:
            if not get_result(answer, arr):
                answer = arr
        return

    for i in range(index, 11):
        if rest >= info[i] + 1:
            temp = arr[:]
            temp[i] = info[i] + 1
            dfs(info, i + 1, rest - info[i] - 1, temp)
        dfs(info, i + 1, rest, arr)


def solution(n, info):
    global answer, point
    answer = []
    point = -1e9
    dfs(info, 0, n, [0] * 11)
    if point <= 0:
        return [-1]
    return answer