T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    avg = sum(arr) // n
    result = 0
    for num in arr:
        if num > avg:
            result += num - avg
    print("#{} {}".format(test_case, result))