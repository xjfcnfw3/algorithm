def get_shape(num):
    n = 1
    x, y = 1, 1
    points.append((x, y))
    num -= 1
    while num:
        x += 1
        y -= 1
        if y == 0:
            n += 1
            x, y = 1, n
        points.append((x, y))
        num -= 1


def get_star(x, y):
    n = x + y - 1
    result = 1
    for i in range(1, n):
        result += i
    while n != y:
        n -= 1
        result += 1
    return result


T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    points = [(0, 0)]
    get_shape(max(a, b))
    point_a, point_b = points[a], points[b]
    point_c = [point_a[0] + point_b[0], point_a[1] + point_b[1]]
    print("#{} {}".format(test_case, get_star(point_c[0], point_c[1])))