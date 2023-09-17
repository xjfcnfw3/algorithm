T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    print("#{} ".format(test_case), end="")
    for i in range(n):
        print("{}/{}".format(1, n), end=" ")
    print()
