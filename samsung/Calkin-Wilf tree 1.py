T = int(input())
for test_case in range(1, T + 1):
    left, right = 1, 1
    for c in input():
        if c == 'R':
            right = left + right
        else:
            left = left + right
    print("#{} {} {}".format(test_case, right, left))