def mul(n, depth):
    if depth == 1:
        return n

    if depth % 2 == 0:
        return mul(n, depth // 2) * mul(n, depth // 2)
    else:
        return mul(n, depth // 2) * mul(n, depth // 2) * n


T = 10
for test_case in range(1, T + 1):
    n = int(input())
    a, b = map(int, input().split())
    print("#" + str(n) + " " + str(mul(a, b)))