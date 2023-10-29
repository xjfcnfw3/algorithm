T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    result = []
    temp = ""

    for v, num in arr:
        num = int(num)
        while num > 0:
            temp += v
            if len(temp) >= 10:
                result.append(temp)
                temp = ""
            num -= 1
    if temp:
        result.append(temp)
    print("#{}".format(test_case))
    for arr in result:
        print("".join(arr))