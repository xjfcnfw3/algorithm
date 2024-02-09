n = int(input())
arr = sorted(list(map(int, input().split())))
number = int(input())
left, right = 0, n - 1
answer = 0
while left < right:
    temp = arr[left] + arr[right]
    if temp <= number:
        if temp == number:
            answer += 1
        left += 1
    else:
        right -= 1
print(answer)