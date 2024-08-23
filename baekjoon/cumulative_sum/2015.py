import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = defaultdict(int)
d[0] = 1
temp = 0
result = 0
for num in arr:
    temp += num

    if temp - k in d:
        result += d[temp - k]

    d[temp] += 1
print(result)