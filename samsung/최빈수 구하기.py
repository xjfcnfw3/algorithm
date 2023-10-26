from collections import Counter
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_num = 0
    for v, num in Counter(arr).items():
        if max_num < num:
            result = v
            max_num = num
        elif max_num == num and result < v:
            result = v
    print("#{} {}".format(n, result))