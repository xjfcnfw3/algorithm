import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
temp = arr[0]
result = 0
while right < n:
    if temp <= m:
        if temp == m:
            result += 1
        right += 1
        if right == n:
            break
        temp += arr[right]
    else:
        temp -= arr[left]
        left += 1
print(result)