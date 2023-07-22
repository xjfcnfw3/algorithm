import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
home = []
chick = []
result = sys.maxsize
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chick.append([i, j])

for c in combinations(chick, m):
    temp = 0
    for h in home:
        chick_len = 999
        for j in range(m):
            chick_len = min(chick_len, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += chick_len
    result = min(result, temp)

print(result)