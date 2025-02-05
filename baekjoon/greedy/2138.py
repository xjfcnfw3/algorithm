n = int(input())
arr = list(map(int, input()))
target = list(map(int, input()))

def check(a, b):
    temp = a[:]
    press = 0

    for i in range(1, n):
        if temp[i - 1] == b[i - 1]:
            continue

        press += 1

        for j in range(i - 1, i + 2):
            if j < n:
                temp[j] = 1 - temp[j]
    if temp == b:
        return press
    return 1e9

result = check(arr, target)
arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]

result = min(result, check(arr, target) + 1)

if result != 1e9:
    print(result)
else:
    print(-1)