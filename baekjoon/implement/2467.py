import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, len(arr) -1

current = sys.maxsize
result = [arr[left], arr[right]]

while left < right:
    num = arr[left] + arr[right]

    if abs(num) < current:
        current = abs(num)
        result = [arr[left], arr[right]]

    if num < 0:
        left += 1
    else:
        right -= 1

print(*result)