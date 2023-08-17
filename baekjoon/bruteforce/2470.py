import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1

answer = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]

while left < right:
    left_val = arr[left]
    right_val = arr[right]

    s = left_val + right_val

    if abs(s) < answer:
        answer = abs(s)
        result = [left_val, right_val]
        if answer == 0:
            break

    if s < 0:
        left += 1
    else:
        right -= 1

print(*result)