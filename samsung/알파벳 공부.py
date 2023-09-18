T = int(input())

for test_case in range(1, T + 1):
    s = list(input())
    result = 1
    if s[0] != 'a':
        print("#{} 0".format(test_case, result))
        continue
    for i in range(len(s)-1):
        if ord(s[i]) + 1 == ord(s[i + 1]):
            result += 1
        else:
            break
    print("#{} {}".format(test_case, result))
