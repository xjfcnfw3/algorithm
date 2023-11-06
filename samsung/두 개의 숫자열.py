T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    result = -1e9
    for i in range(len(b) - len(a) + 1):
        temp = 0
        for j in range(len(a)):
            temp += a[j] * b[i + j]
        result = max(temp, result)
    print("#{} {}".format(test_case, result))