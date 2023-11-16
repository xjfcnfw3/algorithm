def check_before(a, b, c):
    global d, h, m
    if a < d:
        return True
    elif a == d and b < h:
        return True
    elif a == d and h == b and c < m:
        return True
    return False


def check_result(a, b, c):
    global d, h, m
    result = 0
    if c < m:
        b -= 1
        c += 60
    result += c - m
    if b < h:
        a -= 1
        b += 24
    result += (b - h) * 60
    result += (a - d) * 60 * 24
    return result


d, h, m = 11, 11, 11
T = int(input())

for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())

    if check_before(a, b, c):
        print("#{} -1".format(test_case))
    else:
        result = check_result(a, b, c)
        print("#{} {}".format(test_case, result))