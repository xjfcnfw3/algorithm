T = int(input())
for test_case in range(1, T + 1):
    if input().count('x') < 8:
        print("#{} YES".format(test_case))
    else:
        print("#{} NO".format(test_case))