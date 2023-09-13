from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = deque(sorted(list(map(int, input().split()))))
    result = True
    for i in range(n):
        num = (arr[i] // m) * k
        if num < i + 1:
            result = False
            break

    if result:
        print("#{} Possible".format(test_case))
    else:
        print("#{} Impossible".format(test_case))