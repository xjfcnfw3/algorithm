def check(num):
    temp = 2
    while temp <= 1000000 // num:
        result[num * temp] = False
        temp += 1
T = 1
for test_case in range(1, T + 1):
    result = [True] * 1000001
    result[0], result[1] = False, False
    for i in range(2, 1000001):
        if result[i]:
            print(i, end=" ")
            check(i)