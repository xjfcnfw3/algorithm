import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    result = 0
    for num in arr:
        if num < mid:
            continue
        else:
            result += num // mid

    if result >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)