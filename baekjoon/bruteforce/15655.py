from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result =list(combinations(arr, m))
for i in result:
    print(*i)
