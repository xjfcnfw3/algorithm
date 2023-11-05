T = int(input())
for test_case in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    result = p * w
    temp = 0
    if w < r:
        temp = q
    else:
        temp = q + (w - r) * s
    result = min(result, temp)
    print("#{} {}".format(test_case, result))