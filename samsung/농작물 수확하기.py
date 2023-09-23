from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    left, right = n // 2, n // 2
    for i in range(n):
        arr = list(map(int, list(input())))
        for j in range(left, right + 1):
            result += arr[j]
        if i < n // 2:
            left = left - 1
            right = right + 1
        else:
            left = left + 1
            right = right - 1

    print("#" + str(test_case) + " " + str(result))