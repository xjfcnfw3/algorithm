def check(x, y):
    global result
    temp = 0
    for i in range(m):
        temp += sum(arr[x + i][y:y + m])
    result = max(result, temp)

T = int(input())
for test_case in range(1, T + 1):
    result = 0
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            check(i, j)
    print("#{} {}".format(test_case, result))