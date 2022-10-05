from itertools import combinations
n, m = map(int, input().split())
result = list(combinations(list(range(1, n+1)), m))
for i in result:
    print(*i)
