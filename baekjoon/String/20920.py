import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

book = defaultdict(int)

for _ in range(n):
    c = input().strip()
    if len(c) < m:
        continue
    book[c] += 1

result = []

for k, v in book.items():
    result.append((k, v))

result.sort(key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(result)):
    print(result[i][0])