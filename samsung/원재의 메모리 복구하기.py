def change(num):
    if num == 1:
        return 0
    return 1

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, list(input())))
    current = 0
    result = 0
    for num in arr:
        if current != num:
            result += 1
            current = change(current)
    print("#" + str(test_case) + " " + str(result))