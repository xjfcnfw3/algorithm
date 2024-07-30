n = int(input())
arr = list(map(int, input().split()))
s = int(input())
for i in range(n - 1):
    if s == 0:
        break
    max_num, idx = arr[i], i
    for j in range(i + 1, min(n, i + 1 + s)):
        if max_num < arr[j]:
            max_num = arr[j]
            idx = j
    s -= idx-i
    for j in range(idx, i, -1):
        arr[j] = arr[j - 1]
    arr[i] = max_num
print(*arr)