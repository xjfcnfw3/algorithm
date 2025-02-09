
def bisect(num, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] == num:
            return mid
        else:
            right = mid - 1
    return left

n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

for i in range(1, len(arr)):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        lis[bisect(arr[i], lis)] = arr[i]

print(len(lis))