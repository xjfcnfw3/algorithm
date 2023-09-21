def check(arr, i):
    global move
    result = 999
    for m in move:
        if 0 <= i + m < len(arr):
            if arr[i+m] >= arr[i]:
                return 0
            else:
                result = min(result, arr[i]- arr[i + m])
    return result

T = 10

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(n):
        result += check(arr, i)
    print("#"+ str(test_case) + " " + str(result))