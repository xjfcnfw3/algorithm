from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = list(permutations(arr, m))
for i in result:
    print(*i)