T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr) / n
    result = 0
    for num in arr:
        if num <= avg:
            result += 1
    print("#{} {}".format(test_case, result))