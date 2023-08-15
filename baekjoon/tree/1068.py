import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
result = 0

def dfs(index, arr):
    arr[index] = -2
    for i in range(len((arr))):
        if index == arr[i]:
            dfs(i, arr)

dfs(k, arr)

for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        result += 1

print(result)