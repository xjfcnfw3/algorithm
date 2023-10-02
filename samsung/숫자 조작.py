T = int(input())

for test_case in range(1, T + 1):
    n = list(input())
    min_result = int("".join(n))
    max_result = int("".join(n))

    for i in range(len(n)):
        for j in range(len(n)):
            arr = n[:]
            temp = n[i]
            arr[i] = arr[j]
            arr[j] = temp
            if arr[0] == '0':
                continue
            num = int("".join(arr))
            min_result = min(num, min_result)
            max_result = max(num, max_result)
    print("#{} {} {}".format(test_case, min_result, max_result))
