import sys

input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]

arr.sort(key=len)
result = 0

for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if arr[i] == arr[j][0:len(arr[i])]:
            flag = True
            break
    if not flag:
        result += 1
print(result)