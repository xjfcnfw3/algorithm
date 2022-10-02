from itertools import permutations

n, m = map(int, input().split())
for i in permutations(list(range(1, n+1)), m):
    print(*i)