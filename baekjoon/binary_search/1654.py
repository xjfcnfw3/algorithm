k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    line = 0
    for num in arr:
        line += num // mid

    if line >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
