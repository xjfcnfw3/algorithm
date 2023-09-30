def check(num):
    a = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            a = i
    return int(a + num / a - 2)


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print("#{} {}".format(test_case, check(n)))
