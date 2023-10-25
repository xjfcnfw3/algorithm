T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_num = 0

    for i in reversed(range(len(arr))):
        if arr[i] > max_num:
            max_num = arr[i]
        else:
            result += max_num - arr[i]
    print("#{} {}".format(test_case, result))