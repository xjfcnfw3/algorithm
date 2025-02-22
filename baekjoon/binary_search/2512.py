n = int(input())
arr = list(map(int, input().split()))
money = int(input())

start, end = 1, max(arr)
answer = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for num in arr:
        if num > mid:
            temp += mid
        else:
            temp += num
    if temp > money:
        end = mid - 1
    else:
        start = mid + 1
        answer = max(answer, mid)
print(answer)