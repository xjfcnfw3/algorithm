x, y = map(int, input().split())

z = (100 * y) // x

if z >= 99:
    print(-1)
    exit(0)

left, right = 0, x
answer = x

while left <= right:
    mid = (left + right) // 2
    result = (100 * (y + mid)) // (x + mid)
    if result > z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)