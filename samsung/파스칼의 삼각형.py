T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = []
    print("#{}".format(test_case))
    for i in range(1, n + 1):
        arr = []
        if i == 1:
            arr = [1]
        elif i == 2:
            arr = [1, 1]
        else:
            arr = [0] * i
            arr[0] = 1
            arr[-1] = 1
            for j in range(1, i - 1):
                arr[j] = result[i - 2][j - 1] + result[i - 2][j]
        result.append(arr)
        print(*arr)