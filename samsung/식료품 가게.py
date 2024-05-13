T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (n * 2)
    result = []
    for i in range(n * 2):
        if visited[i]:
            continue
        for j in range(i + 1, n * 2):
            if visited[j]:
                continue
            elif arr[j] * 3 // 4 == arr[i]:
                visited[j] = True
                break
        visited[i] =True
        result.append(arr[i])
    print("#{}".format(test_case), end =" ")
    print(*result)
