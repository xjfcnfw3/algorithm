T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    b = bin(b)[2:]
    if len(b) < a:
        print("#{} OFF".format(test_case))
        continue
    result = True
    for i in range(1, a + 1):
        if b[-1 * i] == '0':
            result = False
            break
    if result:
        print("#{} ON".format(test_case))
    else:
        print("#{} OFF".format(test_case))
