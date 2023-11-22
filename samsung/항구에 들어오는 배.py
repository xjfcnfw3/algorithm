T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    temp = []
    for i in range(1, n):
        if arr[i] - 1 not in temp:
            result = False
            for j in temp:
                if (arr[i] - 1) % j == 0:
                    result = True
                    break
            if not result:
                temp.append(arr[i] - 1)
    print("#{} {}".format(test_case, len(temp)))