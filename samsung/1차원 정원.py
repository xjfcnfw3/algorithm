T = int(input())
for test_case in range(1, T + 1):
    n, d = map(int, input().split())
    d = d * 2 + 1
    result = n // d
    if n % d > 0:
        result += 1
    print("#{} {}".format(test_case, result))