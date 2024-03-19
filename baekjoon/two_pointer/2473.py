import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 1e13
answer = []

for left in range(n - 2):
    mid = left + 1
    right = n - 1
    while mid < right:
        current = arr[left] + arr[right] + arr[mid]
        if abs(current) < result:
            answer = [arr[left], arr[mid], arr[right]]
            result = abs(current)
        if current > 0:
            right -= 1
        elif current < 0:
            mid += 1
        else:
            print(answer[0], answer[1], answer[2])
            exit(0)
print(answer[0], answer[1], answer[2])