import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x:(x[0], x[1]))
result = 0
start, end = arr[0][0], arr[0][1]
for i in range(1, len(arr)):
    if end <= arr[i][0]:
        result += end - start
        start, end = arr[i]
    else:
        end = max(arr[i][1], end)
result += end - start
print(result)
