from itertools import combinations
l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
result = combinations(arr, l)
for i in result:
    print(''.join(i))