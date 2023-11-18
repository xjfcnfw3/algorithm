from bisect import bisect_left
T = int(input())

arr = []

def check(num):
    for i in range(2, int(num**1/2) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2, 999):
    if check(i):
        arr.append(i)


for test_case in range(1, T + 1):
    n = int(input())
    idx = bisect_left(arr, n)
    result = 0
    for i in range(idx):
        for j in range(i, idx):
            if arr[i] + arr[j] > n:
                break
            for k in range(j, idx):
                if arr[i] + arr[j] + arr[k] == n:
                    result += 1
                elif arr[i] + arr[j] + arr[k] > n:
                    break
    print("#{} {}".format(test_case, result))