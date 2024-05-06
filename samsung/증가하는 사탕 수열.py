T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    answer = 0
    while b >= c:
        b -= 1
        answer += 1
    while a >= b:
        a -= 1
        answer += 1
    if a == 0 or b == 0 or c == 0:
        print("#{} -1".format(test_case))
    else:
        print("#{} {}".format(test_case, answer))