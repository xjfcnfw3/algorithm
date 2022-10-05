from itertools import product
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = list(product(arr, repeat=m))
for i in result:
    print(*i)