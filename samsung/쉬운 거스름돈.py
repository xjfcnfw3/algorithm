
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    index = 0
    arr = [0] * 8

    while n > 0:
        if n < money[index]:
            index += 1
        else:
            n -= money[index]
            arr[index] += 1
    print("#{}".format(test_case))
    print(*arr)