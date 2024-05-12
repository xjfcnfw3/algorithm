def check(s):
    if s != s[::-1]:
        return False
    if s[:(len(s) - 1) // 2] != s[:(len(s) - 1) // 2][::-1]:
        return False
    if s[(len(s) + 1) // 2:] != s[(len(s) + 1) // 2:][::-1]:
        return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    if check(input()):
        print("#{} YES".format(test_case))
    else:
        print("#{} NO".format(test_case))