e, s, m = map(int, input().split())
result = 1
arr = [1, 1, 1]
while e != arr[0] or s != arr[1] or m != arr[2]:
    arr[0] += 1
    arr[1] += 1
    arr[2] += 1
    result += 1
    if arr[0] > 15:
        arr[0] = 1
    if arr[1] > 28:
        arr[1] = 1
    if arr[2] > 19:
        arr[2] = 1
print(result)
