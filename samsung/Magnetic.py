T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for j in range(n):
        stack = []
        for i in range(n):
            if arr[i][j] == 1:
                stack.append(1)
            elif arr[i][j] == 2 and stack:
                stack.clear()
                result += 1
    print("#{} {}".format(test_case, result))