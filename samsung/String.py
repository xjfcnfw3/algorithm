T = 10
for test_case in range(1, T + 1):
    n = int(input())
    st = input()
    result = len(input().split(st))
    print("#" + str(n) + " " + str(result-1))
