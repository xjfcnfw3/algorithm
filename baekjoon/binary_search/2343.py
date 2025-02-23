n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
answer = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1

    for num in arr:
        if total + num > mid:
            count += 1
            total = 0
        total += num

    if count <= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)