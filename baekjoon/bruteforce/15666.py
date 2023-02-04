n, m = map(int, input().split())
arr = list(map(int, input().split()))
temp = []
arr.sort()


def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    num = 0
    for i in range(start, n):
        if num != arr[i]:
            temp.append(arr[i])
            num = arr[i]
            dfs(i)
            temp.pop()


dfs(0)
