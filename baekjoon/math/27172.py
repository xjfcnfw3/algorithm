import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

nums = [0] * 1000001

result = [0] * n

for i in range(len(arr)):
    nums[arr[i]] = i + 1


for num in sorted(arr):
    for j in range(num * 2, 1000001, num):
        if nums[j] >= 1:
            result[nums[j] - 1] -= 1
            result[nums[num] - 1] += 1

print(*result)
