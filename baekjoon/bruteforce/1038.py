import sys
from itertools import combinations

input = sys.stdin.readline


n = int(input())

result = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = int(''.join(list(map(str, reversed(list(j))))))
        result.append(num)

result.sort()
if n >= len(result):
    print(-1)
else:
    print(result[n])