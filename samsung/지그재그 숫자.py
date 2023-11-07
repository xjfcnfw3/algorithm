T = int(input())
for test_case in range(1, T + 1):
    result = 0
    n = int(input())
    for i in range(1, n + 1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print("#{} {}".format(test_case, result))