n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start, end = min(arr), sum(arr)
max_day = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2
    charge = mid
    num = 1
    for day in arr:
        if charge < day:
            charge = mid
            num += 1
        charge -= day
    if num > m or mid < max_day:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)