import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(n):
    num = arr[i]
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == num:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                result += 1
                break
        elif arr[start] + arr[end] > num:
            end -= 1
        elif arr[start] + arr[end] < num:
            start += 1
print(result)