n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0


def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        num = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= num + mid:
                count += 1
                num = arr[i]
        if count >= c:
            global result
            start = mid + 1
            result = mid
        else:
            end = mid - 1

binary_search(arr, start, end)
print(result)