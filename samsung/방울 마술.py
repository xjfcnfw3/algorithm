T = int(input())
for test_case in range(1, T + 1):
    board, count = input().split()
    count = int(count)
    result = 0
    if board == "o..":
        if count == 0 or count % 2 == 0:
            result = 0
        else:
            result = 1
    elif board == ".o.":
        if count == 0 or count % 2 == 0:
            result = 1
        else:
            result = 0
    else:
        if count == 0:
            result = 2
        elif count % 2 == 0:
            result = 0
        else:
            result = 1
    print("#{} {}".format(test_case, result))