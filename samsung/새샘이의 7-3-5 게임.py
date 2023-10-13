from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    nums_li = []
    for nums in  combinations(arr, r=3):
        result = sum(list(nums))
        if result not in nums_li:
            nums_li.append(result)
    nums_li.sort()
    print("#{} {}".format(test_case, nums_li[-5]))
