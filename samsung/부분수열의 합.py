from itertools import combinations
T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(1, len(arr) + 1):
        for com in combinations(arr, r = i):
            if sum(com) == k:
                result += 1
    print("#{} {}".format(test_case, result))