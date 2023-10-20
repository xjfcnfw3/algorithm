def check(i, j):
    global result
    for dx in range(1, 8-i):
        if m[i + dx][j] == "O":
            result = False
            return
    for dy in range(1, 8-j):
        if m[i][j + dy] == "O":
            result = False
            return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m = []
    num = 0
    result = True
    for _ in range(8):
        arr = list(input())
        for i in range(8):
            if arr[i] == "O":
                num += 1
        m.append(arr)
    if num != 8:
        print("#{} no".format(test_case))
        continue
    for i in range(8):
        for j in range(8):
            if m[i][j] == "O":
                check(i, j)
        if not result:
            break
    if result:
        print("#{} yes".format(test_case))
    else:
        print("#{} no".format(test_case))