def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)
    return result

arr = [1, 2, 3, 4,5]
N = 5

def perm_2(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm_2(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]
perm_2(0)