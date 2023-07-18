import sys
input = sys.stdin.readline

n = int(input())

time = []
result = [-1]
for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x : (x[1], x[0]))

for start, end in time:
    if start >= result[-1]:
        result.append(end)
print(len(result) - 1)