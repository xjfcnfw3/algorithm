T = int(input())

for test_case in range(1, T + 1):
    arr = list(input())
    result = 0
    offset = True
    for i in range(len(arr)):
        if not offset:
            offset = True
            continue
        if arr[i] == "(" and i < len(arr) - 1:
            if arr[i + 1] == ")":
                offset = False
                result += 1
            elif arr[i + 1] == "|":
                result += 1
        elif arr[i] == ")" and i > 0:
            if arr[i - 1] == "(" or arr[i - 1] == "|":
                result += 1
    print("#{} {}".format(test_case, result))
