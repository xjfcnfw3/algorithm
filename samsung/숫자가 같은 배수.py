from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    n = list(input())
    num = int("".join(n))
    result = False
    for c in list(permutations(n, r=len(n))):
        number = int("".join(c))
        if number > num and number % num == 0:
            result = True
            break
    if result:
        print("#{} possible".format(test_case))
    else:
        print("#{} impossible".format(test_case))