import sys

input = sys.stdin.readline
n = int(input())
arr = []
result = 1e9
for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(a, b, index):
    global result
    if index >= len(arr):
        if b > 0:
            result = min(result, abs(a - b))
        return
    dfs(a * arr[index][0], b + arr[index][1], index + 1)
    dfs(a, b, index + 1)

dfs(1, 0, 0)

print(result)